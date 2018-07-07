/*
  https://leetcode.com/problems/search-insert-position/description/
*/

public class SearchInsertPosition {
  
  // WRONG ANSWER: FAIL TO DEAL WITH SOME NON-CORNER CASES
  public static int searchInsert(int[] nums, int target) {
    
    int left = 0, right = nums.length - 1;
    int mid = (left + right) / 2;
    
    if (nums[left] > target) {
      return left;
    }
    
    if (nums[right] < target) {
      return right + 1;
    }
    
    while (mid >= left && mid <= right) {
      if (nums[mid] < target) {
        if (nums[mid + 1] > target) {
          return mid + 1;
        }
        else 
          mid = (mid + 1 + right) / 2;
      }
      else if (nums[mid] > target) {
        if (nums[mid - 1] < target) {
          return mid;
        }
        else
          mid = (left + mid - 1) / 2;
      }
      else {
        return mid;
      }
      
    }
    return mid;
  }
  
  /*
   * binary search will change the make pointer to either side
   * while this method will make pointer to the mid
   * contradict direction*/
  public static int searchInsert2(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    
    // left can equal to the right
    while (left <= right) {
      int mid = (left + right) / 2;
      
      if (nums[mid] == target) {
        return mid;
      }
      else if (nums[mid] < target) {
        left = mid + 1;
      }
      else {
        right = mid - 1;
      }
    }
    
    // notice the return
    return left;
  }
  
  public static void main(String[] args) {
    int[] nums = {1, 3, 4, 5, 6};
    System.out.println(searchInsert2(nums, 7));
  }

}
