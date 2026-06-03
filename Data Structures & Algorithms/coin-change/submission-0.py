class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        cache = [float("INF")]*(amount+1)
        cache[0] = 0

        for coin in coins:
            for i in range(1, amount+1):
                if coin <= i:
                    cache[i] = min(cache[i], cache[i-coin] + 1)

        if cache[amount] == float("INF"): return -1
        return cache[amount]
