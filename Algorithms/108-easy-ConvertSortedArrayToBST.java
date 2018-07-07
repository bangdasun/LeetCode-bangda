/*
  https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
*/

public class ConvertSortedArrayToBST {
  public static TreeNode sortedArrayToBST(int[] nums) {
    
    if (nums.length == 0) {
      return null;
    }
    
    if (nums.length == 1) {
      return new TreeNode(nums[0]);
    }
    
    if (nums.length == 2) {
      TreeNode root = new TreeNode(nums[1]);
      root.left = new TreeNode(nums[0]);
      return root;
    }
    
    int left = 0, right = nums.length - 1;
    int mid = (left + right) / 2;
    
    TreeNode root = new TreeNode(nums[mid]);
    
    // Note that root is excluded
    int[] left_half = new int[mid];
    int[] right_half = new int[right - mid];
    
    for (int i = 0; i < left_half.length; i++)
      left_half[i] = nums[i];
          
    for (int i = 0; i < right_half.length; i++)
      right_half[i] = nums[mid + 1 + i];
      
    root.left = sortedArrayToBST(left_half);
    root.right = sortedArrayToBST(right_half);
    
    return root;
  }

  public static void main(String[] args) {
    int[] nums = {1, 3, 4, 5, 6, 7};
    TreeNode root = sortedArrayToBST(nums);
    
    System.out.println(root.left.left.val);
    System.out.println(root.left.val);
    System.out.println(root.val);
    System.out.println(root.right.left.val);
    System.out.println(root.right.val);
    System.out.println(root.right.right.val);
    
  }
}
