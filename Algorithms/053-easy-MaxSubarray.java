/*
  https://leetcode.com/problems/maximum-subarray/description/
*/

public class MaxSubarray {
  public static int maxSubArray(int[] nums) {
    
    // two pointers is very complicated...
    // I had to check the solution and there is an algorithm called Kadane's algorithm
    // Suppose we've solved the problem for A[1, i-1], how can we extend to A[1, i]?
    // The max sum in the first i elements is either: max sum of A[1, i-1] or: a subarray end at i (max_ending)
    
    int current_max = nums[0], max_ending = nums[0];
    
    for (int i = 1; i < nums.length; i++) {
      // max_ending: subarray end at i
      max_ending = Math.max(max_ending + nums[i], nums[i]);
      current_max = Math.max(current_max, max_ending);
    }
    
    return current_max;
   }

  public static void main(String[] args) {
    int[] nums = {4, -1, 2, 1, -5, 4};
    System.out.println(maxSubArray(nums));
  }
}
