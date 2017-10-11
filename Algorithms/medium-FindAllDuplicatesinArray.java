/*
  https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
*/

import java.util.ArrayList;
import java.util.List;

public class FindAllDuplicatesinArray {
  
  // Without extra space and in O(n) runtime
  public static List<Integer> findDuplicates(int[] nums) {
    List<Integer> output = new ArrayList<>();
    
    /*
     * for val in nums, set nums[val - 1] to be negative num[val - 1]
     * then keep going... if nums[val - 1] is already negative, this val is duplidate.
     * 
     * connect index to the value
     */
    for (int i : nums) {
      int idx = Math.abs(i) - 1;
      if (nums[idx] < 0) 
        output.add(Math.abs(idx + 1));
      nums[idx] = -nums[idx];
    }
    
    return output;
  }

  public static void main(String[] args) {
    int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
    List<Integer> output = findDuplicates(nums);
    System.out.println(output.get(0));
    System.out.println(output.get(1));
    
  }
}
