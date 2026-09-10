class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n = set(nums)
        if len(nums) != len(set_n):
            return True
        return False

