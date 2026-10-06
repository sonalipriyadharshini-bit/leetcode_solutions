//two-sum

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Use a standard nested loop to check all pairs
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        // Return an empty array if no solution is found
        return new int[]{};
    }
}
