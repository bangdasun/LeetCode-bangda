/*
  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
*/

import java.util.HashMap;

public class TwoSum2 {
  public static int[] twoSum(int[] nums, int target) {
    
//    int count = 0;
//    int[] answer = new int[2];
//    int[] complement = new int[nums.length];
//    HashMap<Integer, Integer> lookup = new HashMap<>();
//    for (int i = 0; i < complement.length; i++) {
//      complement[i] = target - nums[i];
//      lookup.put(nums[i], i);
//    }
//    
//    for (int i = 0; i < nums.length; i++) {
//      // note the situation when one value in array is half of the target
//      // cannot deal with 0 case...
//      if (lookup.containsKey(complement[i]) && complement[i] != nums[i]) {
//        answer[count] = i + 1;
//        count += 1;
//      }
//    }
//    
    
    int start = 0, end = nums.length - 1;
    
    while (start < end) {
      if (nums[start] + nums[end] == target) 
        break;
      else if (nums[start] + nums[end] < target) 
        start += 1;
      else 
        end -= 1;
    }
    
    return new int[]{start + 1, end + 1};
  }
  
  public static void main(String[] args) {
    int[] nums = {2, 3, 4};
    int target = 6;
    int[] answer = twoSum(nums, target);
    
    //System.out.println(answer);
    for (int i = 0; i < answer.length; i++) {
      System.out.println(answer[i]);
    }
  }

}
