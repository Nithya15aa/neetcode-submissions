class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_sum = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in two_sum:
                return [two_sum[diff], i]
            
            two_sum[j] = i