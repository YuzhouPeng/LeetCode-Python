def sumIterate(sums,nums, solution, result, target,pos):
    if len(solution) == 4 and sum(solution) == target:
        newsol = solution.copy()
        result.append(newsol)
        return
    elif len(solution)==4:
        return
    for i in range(pos,len(nums)):
        # if(nums[i]+nums[len(nums)-1]* (3-len(solution)+sums < target)):
        #     continue
        # if (nums[i]*(4-len(solution))+sums>target):
        #     return
        solution.append(nums[i])
        sumIterate(sums+nums[i],nums, solution, result, target,i+1)
        solution.pop(-1)

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        visited = []
        solution = []
        result = []
        sorted(nums)
        for i in range(len(nums)):
            visited.append(0)
        if len(nums) == 0:
            return result
        # for i in range(len(nums)):
        #     visited[i]=1
        #     solution.append(nums[i])
        sumIterate(0,nums, solution, result, target, 0)
        for r in result:
            r.sort()

        #     solution.remove(nums[i])
        result2 = [list(t) for t in set(tuple(element) for element in result)]
        return result2

if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([-5,5,4,-3,0,0,4,-2],4))

