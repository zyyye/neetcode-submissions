class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        nums = list(set(nums))
        def findSet(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = findSet(parent[x])
                return parent[x]
        
        def isSameSet(i, j):
            return findSet(i) == findSet(j)

        def unionSet(i, j):
            if not isSameSet(i, j):
                x, y = findSet(i), findSet(j)
                if rank[x] > rank[y]:
                    parent[y] = x
                else:
                    parent[x] = y
                    if rank[x]==rank[y]: 
                        rank[y] = rank[y] + 1 

        parent = list(range(len(nums)))
        rank = [0] * len(nums)

        dct = {}
        for i, j in enumerate(nums):
            dct[j] = i
        for num in nums:
            for neighbor in [num-1, num+1]:
                if neighbor in dct:
                    unionSet(dct[neighbor], dct[num])

        for i in range(len(nums)):
            findSet(i)

        from collections import Counter
        return max(Counter(parent).values())
            
