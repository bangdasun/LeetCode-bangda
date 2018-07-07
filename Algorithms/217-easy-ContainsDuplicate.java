/*
  https://leetcode.com/problems/contains-duplicate/description/
*/

import java.util.HashMap;

public class ContainsDuplicate {
  public static boolean containsDuplicate(int[] nums) {
    
    HashMap<Integer, Integer> dictionary = new HashMap<>();
    int count = 0;
    
    for (int i = 0; i < nums.length; i++) {
      if (!dictionary.containsKey(nums[i])) 
        dictionary.put(nums[i], i);
      else
        count += 1;
    }
    
    return count > 0;
  }

  public static void main(String[] args) {
    int[] nums = {1, 2, 3, 4, 5, 5};
    System.out.println(containsDuplicate(nums));
  }
}
