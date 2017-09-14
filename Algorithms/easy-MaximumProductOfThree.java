/*
  https://leetcode.com/problems/maximum-product-of-three-numbers/description/
*/

import java.util.Arrays;

public class MaximumProductOfThree {
  public static int maximumProduct(int[] nums) {
    Arrays.sort(nums);
    int last = nums.length - 1;
    
    /*
     * let x, y, z to be rightmost of sorted nums and a, b to be leftmost of sorted nums
     * (1) x, y, z > 0 -> max_prod = x * y * z
     * (2) only z > 0 -> x * y * z still positive, but x * y < a * b -> max_prod = z * a * b
     * (3) only y, z > 0 -> max_prod must < 0 -> max_prod = x * y * z
     */
    return Math.max(nums[last] * nums[last - 1] * nums[last - 2], nums[last] * nums[0] * nums[1]);
  }

}
