/*
  https://leetcode.com/problems/detect-capital/description/
*/

public class DetectCapital {
  public static boolean detectCapitalUse(String word) {
    
    if (word.toLowerCase().equals(word) || word.toUpperCase().equals(word)) {
      return true;
    }
    
    if (word.substring(1).toLowerCase().equals(word.substring(1))) {
      return true;
    }
    else {
      return false;
    }
  }
  
  public static void main(String[] args) {
    System.out.println(detectCapitalUse("Google"));
    System.out.println(detectCapitalUse("google"));
    System.out.println(detectCapitalUse("GooGle"));
    System.out.println(detectCapitalUse("GOOGLE"));
    
  }

}
