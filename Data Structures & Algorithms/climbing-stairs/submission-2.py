class Solution:
    import math
    def climbStairs(self, n: int):
        array = [-1]*n
        
        def dfs(i: int):
            if i >= n: return i == n
            if array[i] != -1: return array[i]
            array[i] = dfs(i+1) + dfs(i+2)
            return array[i]
        return dfs(0)