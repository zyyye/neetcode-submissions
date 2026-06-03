class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] # base case

        size = len(nums)-2
        cache = [-1]*(size+2)
        includeFirst = nums[:size+1]
        excludeFirst = nums[1:]

        def dfs(i, df):
            if i > size: return 0
            if i == size: return df[i]

            if cache[i] != -1: return cache[i]
            cache[i] = max(df[i] + dfs(i+2, df), dfs(i+1, df))
            return cache[i]
        option1 = dfs(0, includeFirst)
        cache = [-1]*(size+1)

        return max(option1, dfs(0, excludeFirst))
        