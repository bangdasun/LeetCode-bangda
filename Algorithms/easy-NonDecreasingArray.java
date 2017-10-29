/*
  https://leetcode.com/problems/non-decreasing-array/description/
*/

public class NonDecreasingArray {
  
  /* "Greedy" problem
   * When you find nums[i-1] > nums[i], you will try to change nums[i-1]
   * But if you also find nums[i-2] > nums[i] you will try to change nums[i]
   * */
  public static boolean checkPossibility(int[] nums) {
    
    int count = 0;
    
    for (int i = 1; i < nums.length && count <= 1; i++) {
      if (nums[i - 1] > nums[i]) {
        count ++;
        if (i < 2 || nums[i - 2] <= nums[i])
          nums[i - 1] = nums[i];
        else
          nums[i] = nums[i - 1];
      }
    }
    
    return count <= 1;
  }
  
  public static void main(String[] args) {
    int[] nums1 = {4, 2, 3};
    int[] nums2 = {4, 2, 1};
    int[] nums3 = {-1, 4, 2, 3};
    int[] nums4 = {3, 4, 2, 3};
    int[] nums5 = {3, 2, 2, 3};
        
    System.out.println(checkPossibility(nums1));
    System.out.println(checkPossibility(nums2));
    System.out.println(checkPossibility(nums3));
    System.out.println(checkPossibility(nums4));
    System.out.println(checkPossibility(nums5));
    
  }

}
