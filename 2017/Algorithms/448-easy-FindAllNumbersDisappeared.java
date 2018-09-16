/*
  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/  
*/

import java.util.ArrayList;
import java.util.List;

public class FindAllNumbersDisapperedinArray {
  
  // Without extra space and in O(n) time
  public static List<Integer> findDisappearNumbers(int[] nums) {
    List<Integer> output = new ArrayList<>();
    for (int i: nums) {
      int idx = Math.abs(i) - 1;
      if (nums[idx] > 0) {
        nums[idx] = -nums[idx];
      }
    }
    
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 0) {
        output.add(i + 1);
      }
    }
    
    return output;
  }
  
  public static void main(String[] args) {
    int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
    List<Integer> output = findDisappearNumbers(nums);
    System.out.println(output.get(0));
    System.out.println(output.get(1));
  }

}
