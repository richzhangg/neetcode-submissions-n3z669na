class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lists = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in lists:
                return [lists[diff], i]
            else:
                lists[j] = i
        return