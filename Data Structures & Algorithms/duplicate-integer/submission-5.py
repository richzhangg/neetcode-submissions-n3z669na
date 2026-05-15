class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lists = {}
        for i in nums:
            if i in lists:
                return True
            lists[i] = 1
        return False