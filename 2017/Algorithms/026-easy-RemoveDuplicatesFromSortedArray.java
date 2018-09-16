/*
  https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
*/
public class RemoveDuplicates {
  public static int removeDuplicates(int[] nums) {
    // nums is sorted
    int count = 0;
    
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] != nums[i - 1]) {
        count += 1;
        nums[count] = nums[i];    
      }
    }

    return count + 1;
  }
  
  public static void main(String[] args) {
    int[] nums = {1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6};
    int answer = removeDuplicates(nums);
    
    System.out.println(answer);
  }

}
