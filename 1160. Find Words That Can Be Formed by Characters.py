class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        # create a count map from chars
        # counting the word and stop if any letter count go over the source count
        def isValid(word, cnt):
            count = collections.defaultdict(int)
            for c in word:
                if c not in cnt:
                    return False
                else:
                    count[c] += 1
                    if count[c] > cnt[c]:
                        return False
            return True

        cnt = collections.Counter(chars)
        res = 0
        for word in words:
            if isValid(word, cnt):
                res += len(word)
        return res