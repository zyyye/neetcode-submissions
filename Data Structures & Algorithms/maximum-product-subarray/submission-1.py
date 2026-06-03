class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        currMax = nums[0]
        currMin = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            currPointer = nums[i]
            A = currMax*currPointer
            B = currMin*currPointer
            currMax = max(A, B, currPointer)
            currMin = min(A, B, currPointer)
            globalMax = max(currMax, globalMax)

        return globalMax


        
        