/*
  https://leetcode.com/problems/first-unique-character-in-a-string/description/ 
*/
public class FirstUniqueCharacterinString {
  
  // WRONG: cannot output -1
  public static int firstUniqChar(String s) {
    
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
      if (s.charAt(left) != s.charAt(right)) {
        right --;
      }
      else {
        left ++;
        right = s.length() - 1;
      }
    }
    
    return left;
  }
  
  // A STRAIGHTFORWARD SOL: https://leetcode.com/problems/first-unique-character-in-a-string/discuss/
  public static int firstUniqChar2(String s) {
    int freq[] = new int[26];
    
    for (int i = 0; i < s.length(); i++) {
      freq[s.charAt(i) - 'a'] ++;
    }
    
    for (int i = 0; i < s.length(); i++) {
      if (freq[s.charAt(i) - 'a'] == 1) {
        return i;
      }
    }
    
    return -1;
  }
  
  public static void main(String[] args) {
    String s1 = "leetcode";
    String s2 = "loveleetcode";
    System.out.println(firstUniqChar2(s1));
    System.out.println(firstUniqChar2(s2));
  }

}
