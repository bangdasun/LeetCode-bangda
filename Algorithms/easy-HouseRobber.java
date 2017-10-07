/*
  https://leetcode.com/problems/house-robber/description/
*/

public class HouseRobber {
  public static int rob(int[] nums) {
    // amount of money if rob; no rob
    int include = 0, exclude = 0;
    
    for (int i : nums) {
      int curr_include = exclude + i; // rob current: current + exclude prev
      exclude = Math.max(include, exclude); // don't rob current: exclude prev or include prev
      include = curr_include; // udpate
    }
    
    return Math.max(include, exclude);
  }
  
  public static void main(String[] args) {
    int[] nums = {3, 4, 4, 6, 8, 9, 7, 10, 5};
    System.out.println(rob(nums));
  }

}
