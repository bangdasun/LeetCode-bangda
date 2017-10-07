/*
  https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
*/

public class MaximumDepthofBinaryTree {
  public static int maxDepth(TreeNode root) {
    
    if (root == null) {
      return 0;
    }
    
    return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
  }

}
