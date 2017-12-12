from pkg_resources import get_distribution

from .prediction_algorithms import AlgoBase
from .prediction_algorithms import NormalPredictor
from .prediction_algorithms import BaselineOnly
from .prediction_algorithms import KNNBasic
from .prediction_algorithms import KNNWithMeans
from .prediction_algorithms import KNNWithZScore
from .prediction_algorithms import KNNBaseline
from .prediction_algorithms import SVD
from .prediction_algorithms import SVDpp
from .prediction_algorithms import NMF
from .prediction_algorithms import SlopeOne
from .prediction_algorithms import CoClustering

from .prediction_algorithms import PredictionImpossible
from .prediction_algorithms import Prediction

from .dataset import Dataset
from .dataset import Reader
from .dataset import Trainset
from .evaluate import evaluate
from .evaluate import print_perf
from .evaluate import GridSearch
from . import dump

__all__ = ['AlgoBase', 'NormalPredictor', 'BaselineOnly', 'KNNBasic',
           'KNNWithMeans', 'KNNBaseline', 'SVD', 'SVDpp', 'NMF', 'SlopeOne',
           'CoClustering', 'PredictionImpossible', 'Prediction', 'Dataset',
           'Reader', 'Trainset', 'evaluate', 'print_perf', 'GridSearch',
           'dump', 'KNNWithZScore']

__version__ = get_distribution('scikit-surprise').version

class DatasetAutoFolds(Dataset):
    """A derived class from :class:`Dataset` for which folds (for
    cross-validation) are not predefined. (Or for when there are no folds at
    all)."""

    def __init__(self, ratings_file=None, reader=None, df=None):

        Dataset.__init__(self, reader)
        self.has_been_split = False  # flag indicating if split() was called.

        if ratings_file is not None:
            self.ratings_file = ratings_file
            self.raw_ratings = self.read_ratings(self.ratings_file)
        elif df is not None:
            self.df = df
            self.raw_ratings = [(uid, iid, float(r) + self.reader.offset, None)
                                for (uid, iid, r) in
                                self.df.itertuples(index=False)]
        else:
            raise ValueError('Must specify ratings file or dataframe.')

    def build_full_trainset(self):
        """Do not split the dataset into folds and just return a trainset as
        is, built from the whole dataset.

        User can then query for predictions, as shown in the :ref:`User Guide
        <train_on_whole_trainset>`.

        Returns:
            The :class:`Trainset`.
        """

        return self.construct_trainset(self.raw_ratings)

    def raw_folds(self):

        if not self.has_been_split:
            self.split()

        def k_folds(seq, n_folds):
            """Inspired from scikit learn KFold method."""

            start, stop = 0, 0
            for fold_i in range(n_folds):
                start = stop
                stop += len(seq) // n_folds
                if fold_i < len(seq) % n_folds:
                    stop += 1
                yield seq[:start] + seq[stop:], seq[start:stop]

        return k_folds(self.raw_ratings, self.n_folds)

    def split(self, n_folds=5, shuffle=True):
        """Split the dataset into folds for future cross-validation.

        If you forget to call :meth:`split`, the dataset will be automatically
        shuffled and split for 5-folds cross-validation.

        You can obtain repeatable splits over your all your experiments by
        seeding the RNG: ::

            import random
            random.seed(my_seed)  # call this before you call split!

        Args:
            n_folds(:obj:`int`): The number of folds.
            shuffle(:obj:`bool`): Whether to shuffle ratings before splitting.
                If ``False``, folds will always be the same each time the
                experiment is run. Default is ``True``.
        """

        if n_folds > len(self.raw_ratings) or n_folds < 2:
            raise ValueError('Incorrect value for n_folds. Must be >=2 and '
                             'less than the number or entries')

        if shuffle:
            random.shuffle(self.raw_ratings)

        self.n_folds = n_folds
        self.has_been_split = True


class Reader():
    """The Reader class is used to parse a file containing ratings.

    Such a file is assumed to specify only one rating per line, and each line
    needs to respect the following structure: ::

        user ; item ; rating ; [timestamp]

    where the order of the fields and the separator (here ';') may be
    arbitrarily defined (see below).  brackets indicate that the timestamp
    field is optional.


    Args:
        name(:obj:`string`, optional): If specified, a Reader for one of the
            built-in datasets is returned and any other parameter is ignored.
            Accepted values are 'ml-100k', 'ml-1m', and 'jester'. Default
            is ``None``.
        line_format(:obj:`string`): The fields names, in the order at which
            they are encountered on a line. Default is ``'user item rating'``.
        sep(char): the separator between fields. Example : ``';'``.
        rating_scale(:obj:`tuple`, optional): The rating scale used for every
            rating.  Default is ``(1, 5)``.
        skip_lines(:obj:`int`, optional): Number of lines to skip at the
            beginning of the file. Default is ``0``.

    """

    def __init__(self, name=None, line_format='user item rating', sep=None,
                 rating_scale=(1, 5), skip_lines=0):

        if name:
            try:
                self.__init__(**BUILTIN_DATASETS[name].reader_params)
            except KeyError:
                raise ValueError('unknown reader ' + name +
                                 '. Accepted values are ' +
                                 ', '.join(BUILTIN_DATASETS.keys()) + '.')
        else:
            self.sep = sep
            self.skip_lines = skip_lines
            self.rating_scale = rating_scale

            lower_bound, higher_bound = rating_scale
            self.offset = -lower_bound + 1 if lower_bound <= 0 else 0

            splitted_format = line_format.split()

            entities = ['user', 'item', 'rating']
            if 'timestamp' in splitted_format:
                self.with_timestamp = True
                entities.append('timestamp')
            else:
                self.with_timestamp = False

            # check that all fields are correct
            if any(field not in entities for field in splitted_format):
                raise ValueError('line_format parameter is incorrect.')

            self.indexes = [splitted_format.index(entity) for entity in
                            entities]

    def parse_line(self, line):
        '''Parse a line.

        Ratings are translated so that they are all strictly positive.

        Args:
            line(str): The line to parse

        Returns:
            tuple: User id, item id, rating and timestamp. The timestamp is set
            to ``None`` if it does no exist.
            '''

        line = line.split(self.sep)
        try:
            if self.with_timestamp:
                uid, iid, r, timestamp = (line[i].strip()
                                          for i in self.indexes)
            else:
                uid, iid, r = (line[i].strip()
                               for i in self.indexes)
                timestamp = None

        except IndexError:
            raise ValueError('Impossible to parse line. Check the line_format'
                             ' and sep parameters.')

        return uid, iid, float(r) + self.offset, timestamp

