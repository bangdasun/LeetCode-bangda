/*
  https://leetcode.com/problems/single-number/description/
*/

import java.util.HashMap;

// NOT ACCEPTED: WRONG ANSWER
public class SinglNumber {
  public static int singleNumber1(int[] nums) {
    
    int answer = 0;
    HashMap<Integer, Integer> map1 = new HashMap<>();
    HashMap<Integer, Integer> map2 = new HashMap<>();
    
    for (int i = 0; i < nums.length; i++) {
      map1.put(nums[i], i);
    }
    
    for (int i = nums.length - 1; i >= 0; i--) {
      map2.put(nums[i], i);
    }
    
   for (int i = 0; i < nums.length; i++) {
     if (map1.get(nums[i]) == map2.get(nums[i])) {
       answer = nums[i];
     }
   }
   
   return answer;
  }
  
  public static void main(String[] args) {
    int[] nums = {1, 1, 2, 2, 4, 3, 4, 6, 6, -1, -1};
    int answer = singleNumber1(nums);
    System.out.println(answer);
  }

}
