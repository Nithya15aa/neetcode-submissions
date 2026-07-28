class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0 

        hashset = set(nums)

        for i in nums:
            
            if i-1 not in hashset:
                curr = i
                length =1

                while curr+1 in hashset:
                    curr += 1 
                    length += 1

                longest = max(length, longest)
        return longest 
                    

                   