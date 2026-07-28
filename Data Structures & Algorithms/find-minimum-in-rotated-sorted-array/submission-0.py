class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r =  len(nums) -1

        smallest = nums[l]

        
        while l < r:
            mid = l + ((r-l) // 2)
            if nums[mid] > nums[l] and nums [mid] > nums[r]:
                smallest = min(smallest,nums[l],nums[r])
                l = mid 
            else:
                smallest = min(smallest,nums[l],nums[r])
                r = mid 
                
        return smallest
            
                


        