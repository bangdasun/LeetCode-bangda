/*
  https://leetcode.com/problems/two-sum/description/
*/

import java.util.HashMap;

public class TwoSum {
	
  /*
   * Brute Force 
   * */
  public static int[] twoSum1(int[] nums, int target) {
		
    int[] answer = new int[2];
		
    for (int i = 0; i < nums.length - 1; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (target == nums[i] + nums[j]) {
          answer[0] = i;
          answer[1] = j; 
        }
      }
    }
	    
    return answer;
  }
	
  /*
   * Apply HashMap
  **/
  public static int[] twoSum2(int[] nums, int target) {
	
    HashMap<Integer, Integer> lookup = new HashMap<>();
    int[] answer = new int[2];
	
    for (int i = 0; i < nums.length; i++) {
	  lookup.put(nums[i], i);
    }
	
    for (int i = 0; i < nums.length; i++) {
    int right = target - nums[i];
      if (lookup.containsKey(right) && lookup.get(right) != i) {
        answer[0] = i;
        answer[1] = lookup.get(right);
        break;
      }
    }
	
    return answer;
  }

  public static void main(String[] args) {
	
    int[] nums = {3, 2, 4};
    int target = 6;
    int[] answer1 = twoSum1(nums, target);
    int[] answer2 = twoSum2(nums, target);

    System.out.println("*** Solution for Brute Force ***");
    for (int i = 0; i < answer1.length; i++) {
      System.out.println(answer1[i]);
	}
	
    System.out.println("*** Solution for applying HashMap ***");
    for (int i = 0; i < answer2.length; i++) {
      System.out.println(answer2[i]);
    }
  }
}
