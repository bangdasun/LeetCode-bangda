/*
  https://leetcode.com/problems/symmetric-tree/description/
*/

public class SymmetricTree {
  public static boolean isSymmetric(TreeNode root) {
    return root == null || isMirror(root.left, root.right);
  }
  
  // help function
  public static boolean isMirror(TreeNode left, TreeNode right) {
    if (left == null || right == null) {
      return left == right;
    }
  
    return left.val == right.val && (isMirror(left.left, right.right) && isMirror(left.right, right.left)); 
  }
}
