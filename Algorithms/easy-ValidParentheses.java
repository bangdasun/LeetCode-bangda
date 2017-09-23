/*
  https://leetcode.com/problems/valid-parentheses/description/
*/

import java.util.Stack;

public class ValidParentheses {
  public static boolean isValid(String s) {
    String[] char_lst = s.split("");
    Stack<String> stack = new Stack<>();
    
    for (int i = 0; i < char_lst.length; i++) {
      if (char_lst[i].equals("(") || char_lst[i].equals("{") || char_lst[i].equals("[")) {
        stack.push(char_lst[i]);
      }
      else if (char_lst[i].equals(")")) {
        if (!stack.isEmpty()) {
          String left = stack.pop();
          if (!left.equals("(")) {
            return false;
          }
        } else {
          return false;
        }
      }
      else if (char_lst[i].equals("}")) {
        if (!stack.isEmpty()) {
          String left = stack.pop();
          if (!left.equals("{")) {
            return false;
          }
        } else {
          return false;
        }
      }
      else if (char_lst[i].equals("]")) {
        if (!stack.isEmpty()) {
          String left = stack.pop();
          if (!left.equals("[")) {
            return false;
          }
        } else {
          return false;
        }
      }
    }
    
    return stack.isEmpty();
  }
  
  public static void main(String[] args) {
    System.out.println(isValid("[2134324(3214324{)]"));
  }

}
