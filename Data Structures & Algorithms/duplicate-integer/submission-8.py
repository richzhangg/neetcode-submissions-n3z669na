class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = {}
        for i in nums:
            if i in sets:
                return True
            else:
                sets[i] = 1
        return False