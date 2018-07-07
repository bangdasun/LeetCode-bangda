/*
  https://leetcode.com/problems/majority-element/discuss/
*/

import java.util.Arrays;

public class MajorityElement {
  public static int majorityElement(int[] nums) {
    Arrays.sort(nums);
    int mid = nums.length / 2;
    return nums[mid];
  }
  
  // more solutions... https://leetcode.com/problems/majority-element/discuss/
  
  public static void main(String[] args) {
    int[] nums = {6, 6, 6, 6, 1, 2, 6, 6, 6, 6};
    System.out.println(majorityElement(nums));
  }

}
