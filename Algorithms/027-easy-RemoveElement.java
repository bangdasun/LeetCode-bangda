/*
  https://leetcode.com/problems/remove-element/description/
*/
public class RemoveElement {
  public static int removeElement(int[] nums, int val) {
    
    int count = 0;
    
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != val) {
        nums[count] = nums[i];
        count += 1;
      }
    }
    
    return count;
  }
  
  public static void main(String[] args) {
    int[] nums = {3, 2, 2, 3};
    int val = 3;
    int answer = removeElement(nums, val);
    System.out.println(answer);
    
  }

}

// see also Approach #2 
