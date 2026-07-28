class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r =  len(nums) -1

        smallest = nums[l]

        
        while l < r:
            mid = l + ((r-l) // 2)
            if nums [mid] > nums[r]:
                smallest = min(smallest,nums[mid],nums[r])
                l = mid + 1
            else:
                smallest = min(smallest,nums[mid],nums[l])
                r = mid -1
                
        return smallest
            
                


        