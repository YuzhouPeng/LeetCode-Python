import collections
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        results = []

        w = [word.count(min(word)) for word in words]
        w.sort()
        #.sort()
        for query in queries:
            cnt = query.count(min(query))
            indx = bisect.bisect(w,cnt)
            results.append(len(w)-indx)
        return results