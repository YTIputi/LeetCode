from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i
        return []

class TwoSum:
    def __init__(self):
        s = Solution()
        print(s.twoSum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    TwoSum()