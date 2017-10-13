/*
  https://leetcode.com/problems/binary-tree-inorder-traversal/description/
*/

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreeInorderTraversal {
  
  // Without recursion
  public static List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> out = new ArrayList<>();
    Stack<TreeNode> stk = new Stack<>();
    TreeNode curr = root;
    
    while (curr != null || stk.size() > 0) {
      while (curr != null) {
        stk.push(curr);
        curr = curr.left;
      }
      
      curr = stk.pop();
      out.add(curr.val);
      curr = curr.right;
    }
    
    return out;
  }

}
