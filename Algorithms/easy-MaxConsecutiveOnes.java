/*
  https://leetcode.com/problems/max-consecutive-ones/description/
*/

public class MaxConsecutiveOnes {
  public static int findMaxConsecutiveOnes(int[] nums) {
    int curr_con = 0, max_con = 0;
    
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) {
        curr_con += 1;
      }
      else {
        if (max_con < curr_con)
          max_con = curr_con;
        
         curr_con = 0;
       }
    }
    
    return Math.max(max_con, curr_con); 
  }
  
  public static void main(String[] args) {
    int[] nums = {0};
    System.out.println(findMaxConsecutiveOnes(nums));
  }

}
