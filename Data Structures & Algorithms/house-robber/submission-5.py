class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxm = nums[0]
        f = [None]*len(nums)
        f[0] = nums[0] 
        f[1] = max(f[0], nums[1])
    
        for i in range(2, len(nums)):
            f[i] =  max(f[i-2]+nums[i],f[i-1])
            maxm = max(maxm, f[i])
        return f[-1]