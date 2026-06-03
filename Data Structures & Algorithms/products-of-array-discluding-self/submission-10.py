class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        toRight, toLeft = [1], [1]
        for i in range(1, l):
            toRight.append(toRight[i - 1]*nums[i - 1])
            toLeft.append(toLeft[i - 1]*nums[l - i])
        toLeft = toLeft[::-1]

        res = [1]*l
        for j in range(l):
            res[j] = toRight[j] * toLeft[j] 
        return res


            
            