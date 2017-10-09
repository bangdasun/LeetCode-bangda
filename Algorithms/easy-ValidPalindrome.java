/*
  https://leetcode.com/problems/valid-palindrome/description/
*/

public class ValidPalindrome {
  public static boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    String[] str_list = s.split("");
    String punct = "`.,:;'\"[]{}()-_?!~<>/ @#$%^&*+=|\\";
    
    while (left <= right) {
      if (punct.contains(str_list[left])) {
        left ++;
      }
      else if (punct.contains(str_list[right])) {
        right --;
      }
      else if (str_list[left].toLowerCase().equals(str_list[right].toLowerCase())) {
        left ++;
        right --;
      }
      else {
        return false;
      }
    }
    
    return true;
  }
  
  public static void main(String[] args) {
    String s = "aA.";
    String s1 = "`l;`` 1o1 ??;l`";
    System.out.println(isPalindrome(s));
  }
}
