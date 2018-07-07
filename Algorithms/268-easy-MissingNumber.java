/*
  https://leetcode.com/problems/missing-number/description/
*/

import java.util.HashMap;

public class MissingNumber {
  public static int missingNumber(int[] nums) {
    
    HashMap<Integer, Integer> map = new HashMap<>();
    int missing = 0;
    
    for (int i = 0; i < nums.length; i++) {
      map.put(nums[i], i);
    }
    
    for (int i = 0; i < nums.length; i++) {
      if (!map.containsKey(nums[i] + 1) && nums[i] < nums.length) {
        missing = nums[i] + 1;

      } 
      else if (!map.containsKey(nums[i] - 1) && nums[i] > 0) {
        missing = nums[i] - 1;
      }
    }
    
    return missing;
  }
  
  public static void main(String[] args) {
    int[] nums = {1};
    System.out.println(missingNumber(nums));
  }

}
