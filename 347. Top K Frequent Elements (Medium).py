def getordefault(hashmap,key):
    if key in hashmap:
        hashmap[key] = hashmap[key]+1
        return hashmap
    else:
        hashmap[key] = 1
        return hashmap

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequencymap = {}
        for num in nums:
            getordefault(frequencymap,num)
        buckets = [[] for j in range(len(nums)+1)]
        for key in frequencymap:
            frequency = frequencymap[key]
            buckets[frequency].append(key)
        topk = []
        for i in range(len(buckets)-1,-1,-1):
            if len(topk)<k and buckets[i]!=None:
                topk.extend(buckets[i])
        return topk

# if __name__ == '__main__':
#     sol  = Solution
#     sol.topKFrequent(sol,)

