class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n = set()
        for i in nums:
            if i not in set_n:
                set_n.add(i)
            else:
                return True
        return False
        