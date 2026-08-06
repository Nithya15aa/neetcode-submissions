class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = collections.defaultdict(int)
        for i in nums:
            res[i] += 1

        output = sorted(res.items(), key=lambda x: x[1], reverse=True)
    
        result = []
        for i in range(k):
            result.append(output[i][0]) 
    
        return result
        
        #Store the freq of values in a hashmap. iterate with k to add key to the result with highest value in map .


        