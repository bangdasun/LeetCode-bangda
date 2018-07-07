/*
  https://leetcode.com/problems/product-of-array-except-self/description/
*/

public class ProductOfArrayExceptSelf {
  public static int[] productExceptSelf(int[] nums) {
    int[] results = new int[nums.length];
    
    // get cumulative product
    results[0] = 1;
    for (int i = 1; i < nums.length; i++) {
      results[i] = results[i - 1] * nums[i - 1];
    }
    
    // continuing filling - another "cumulative product"
    int right_part = 1;
    for (int i = nums.length - 1; i >= 0; i--) {
      results[i] = results[i] * right_part;
      right_part = right_part * nums[i];
    }
    
    return results;
  }
  
  public static void main(String[] args) {
    int[] nums = {1, 2, 3, 4};
    int[] results = productExceptSelf(nums);
    for (int i: results) {
      System.out.println(i);
    }
  }
}
