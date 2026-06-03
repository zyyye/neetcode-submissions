class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        cache = [-1]*size

        def dfs(i):
            if i >= size: return 0
            if i == size-1: return nums[i]

            if cache[i] != -1: return cache[i]
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]

        return dfs(0)
        