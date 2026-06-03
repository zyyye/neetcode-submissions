class Solution:
    import math
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        ways, twos = 1, 1
        while True: 
            if twos*2 == n: 
                ways += 1
                break
            if twos*2 + 1 == n: 
                ways += int(math.factorial(n-twos)/math.factorial(twos))
                break

            ways += int(math.factorial(n-twos)/(math.factorial(twos)*math.factorial(n - 2*twos)))
            twos += 1

        return ways