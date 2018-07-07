/*
   https://leetcode.com/problems/merge-sorted-array/description/
 */

public class MergeSortedArray {
  
  // This approach is complicated in dealing with edge condition
  // e.g.: nums1 = {0}, m = 0, nums2 = {1}, n = 1;
  public static void merge(int[] nums1, int m, int[] nums2, int n) {
    int pointer1 = m - 1, pointer2 = n - 1;
    
    if (pointer1 <= 0) {
      nums1 = nums2;
      return;
    } 
    
    if (pointer2 < 0) {
      return;
    }
   
    for (int i = m + n - 1; i >= 0; i--) {
      if (nums1[pointer1] >= nums2[pointer2]) {
        nums1[i] = nums1[pointer1];
        if (pointer1 > 0) {
          pointer1--;
        } 
      }
      else {
        nums1[i] = nums2[pointer2];
        if (pointer2 > 0) {
          pointer2--;
        }
      }
    }
    
    if (pointer1 == 0 && pointer2 >= 0) {
      for (int i = pointer2; i >= 0; i--) {
        nums1[i] = nums2[i];
      }
    }
    
  }
  
  // Better solution
  public static void merge2(int[] nums1, int m, int[] nums2, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 && j >= 0) {
      // ?: operator, like ifelse in R
      // x = (expr) ? value if true: value if false
      // https://www.tutorialspoint.com/java/java_basic_operators.htm
      nums1[k--] = (nums1[i] > nums2[j]) ? nums1[i--] : nums2[j--];
    }
    
    while (j >= 0) {
      nums1[k--] = nums2[j--];
    }
  }
  
  
  public static void main(String[] args) {
    
    int[] nums1 = {0};
    int[] nums2 = {1};
    int m = 0, n = 1;
    
    merge2(nums1, m, nums2, n);
    for (int i = 0; i < m + n; i++) {
      System.out.println(nums1[i]);
    }
    
  }
}
