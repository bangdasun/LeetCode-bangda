/*
  https://leetcode.com/problems/repeated-substring-pattern/description/
*/

public class RepeatedSubstringPattern {
  public static boolean repeatedSubstringPattern(String s) {
    int len = s.length();
    
    if (len == 1)
      return false;
    
    // start from middle, since len % 0 is not defined
    // and we need go backwards (0 is not included since single string should return false;
    for (int i = len / 2; i >= 1; i --) {
      if (len % i == 0) {
        int t = len / i;
        String sub = s.substring(0, i);
        StringBuilder strb = new StringBuilder();
        for (int r = 1; r <= t; r ++)
          strb.append(sub);
       
        if (strb.toString().equals(s))
          return true;
        
        // no else clause, why? if there is a else clause, it will return false for "ababab"
      }
    }
    
    return false;
  }
  
  public static void main(String[] args) {
//    String s1 = "abcabc";
//    String s2 = "abc";
//    String s3 = "a";
    String s4 = "ababab";
//    System.out.println(repeatedSubstringPattern(s1));
//    System.out.println(repeatedSubstringPattern(s2));
//    System.out.println(repeatedSubstringPattern(s3));
    System.out.println(repeatedSubstringPattern(s4));
    
  }

}
