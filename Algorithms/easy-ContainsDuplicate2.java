/*
  https://leetcode.com/problems/contains-duplicate-ii/description/
*/

import java.util.HashMap;

public class ContainsDuplicate2 {
  public static boolean containsNearbyDuplicate(int[] nums, int k) {
    
    HashMap<Integer, Integer> map = new HashMap<>();
    int count = 0;
    
    // notice the case that there are multiple duplicates
    // notice the case that there is only one element in array
    for (int i = 0; i < nums.length; i++) {
      
      if (!map.containsKey(nums[i])) {
        map.put(nums[i], i);
      } 
      else {
        if (i - map.get(nums[i]) <= k) {
          map.put(nums[i], i); // update location
          count += 1;
        }
        else {
          map.put(nums[i], i); // update location
        }
      }
        
    }
    
    return count > 0 && nums.length > 1;
    
  }
  
  public static void main(String[] args) {
    int[] nums1 = {1, 0, 1, 1}; // true
    int[] nums2 = {1}; // false
    int k = 1;
    System.out.println(containsNearbyDuplicate(nums1, k));
    System.out.println(containsNearbyDuplicate(nums2, k));
  }

}
