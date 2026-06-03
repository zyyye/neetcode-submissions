class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = [-1]*len(cost)
        step = len(cost)

        def dfs(n):
            if n >= step: return 0
            if n in [step-1, step-2]: return cost[n]
            if cache[n] != -1: return cache[n]
            cache[n] = cost[n] + min(dfs(n+1), dfs(n+2))
            return cache[n]

        return min(dfs(0),dfs(1))
        