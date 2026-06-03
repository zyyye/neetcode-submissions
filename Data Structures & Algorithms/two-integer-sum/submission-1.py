class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, j in enumerate(nums):
            require = target - j
            if require in dct:
                return [dct[require], i]
            else:
                dct[j] = i
    
        