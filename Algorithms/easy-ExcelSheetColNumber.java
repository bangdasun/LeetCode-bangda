/*
  https://leetcode.com/problems/excel-sheet-column-number/description/
*/

import java.util.HashMap;

public class ExcelSheetColNumber {
  
  public static int titleToNumber(String s) {
    
    char[] lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
    HashMap<Character, Integer> map = new HashMap<>();
    int val = 0;
    
    for (int i = 0; i < 26; i++) {
      map.put(lookup[i], i + 1);
    }
    
    
    for (int i = s.length() - 1; i >= 0; i--) {
      val += map.get(s.charAt(i)) * Math.pow(26, s.length() - 1 - i);
    }
    
    return val;
  }
  
  // more space saving methods: https://leetcode.com/problems/excel-sheet-column-number/discuss/
  
  public static void main(String[] args) {
    
    String title = "I";
    //for (int i = title.length() - 1; i >= 0; i--) {
    //  System.out.println(title.charAt(i));  
    //}
    System.out.println(titleToNumber(title));
    
  }
}
