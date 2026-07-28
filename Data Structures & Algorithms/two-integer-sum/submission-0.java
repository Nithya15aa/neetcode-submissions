

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store the number and its index
        Map<Integer, Integer> seen = new HashMap<>();
        
        // Loop through the nums array
        for (int i = 0; i < nums.length; i++) {
            // Calculate the complement
            int complement = target - nums[i];
            
            // Check if the complement exists in the map
            if (seen.containsKey(complement)) {
                // Return the indices of the two numbers
                return new int[] {seen.get(complement), i};
            }
            
            // Add the current number and its index to the map
            seen.put(nums[i], i);
        }
        
        // Return an empty array if no solution is found
        return new int[] {};
    }
}
