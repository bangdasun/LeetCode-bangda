/*
  https://leetcode.com/problems/set-mismatch/description/
*/

import java.util.HashMap;

// Similar to the MissingNumber.java
// The difference is in this problem number start from 1
public class SetMisMatch {
  public static int[] findErrorNums(int[] nums) {
    
    int[] ans = new int[2];
    HashMap<Integer, Integer> map = new HashMap<>();
    
    for (int i = 0; i < nums.length; i++) {
      
      if (!map.containsKey(nums[i])) {
        map.put(nums[i], i);  
      } else {
        ans[0] = nums[i];
        map.put(nums[i], i);
      }
      
    }
    
    for (int i = 0; i < nums.length; i++) {
      if (!map.containsKey(nums[i] + 1) && nums[i] < nums.length) {
        ans[1] = nums[i] + 1;
      }
      else if (!map.containsKey(nums[i] - 1) && nums[i] > 1) { // notice the minimum number is 1
        ans[1] = nums[i] - 1;
      }
    }
    
    return ans;
  }
  
  // Better implementation using HashTable
  // https://leetcode.com/problems/set-mismatch/solution/
  
  public static void main(String[] args) {
    
    int[] nums = {1, 5, 3, 2, 2, 7, 6, 4, 8 ,9};
    //int[] nums = {3, 5, 9, 4, 1, 2, 7, 8, 1};
    //int[] nums = {1, 2, 2, 4};
    System.out.println(findErrorNums(nums)[0]);
    System.out.println(findErrorNums(nums)[1]); 
  }

}
