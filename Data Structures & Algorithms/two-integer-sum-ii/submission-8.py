class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1, pointer2 = 0, len(numbers) - 1
        while pointer2 > pointer1:
            x, y = numbers[pointer1], numbers[pointer2]
            if x + y == target:
                return [pointer1 + 1, pointer2 + 1]
            elif x + y < target:
                pointer1 += 1
            else:
                pointer2 -= 1

        return []
        