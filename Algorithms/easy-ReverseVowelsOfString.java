/*
  https://leetcode.com/problems/reverse-vowels-of-a-string/description/
*/

import java.util.ArrayList;

public class ReverseVowelsOfString {
  public static String reverseVowels(String s) {
    
    ArrayList<Character> vowels = new ArrayList<>();
    vowels.add('a');
    vowels.add('e');
    vowels.add('i');
    vowels.add('o');
    vowels.add('u');
    vowels.add('A');
    vowels.add('E');
    vowels.add('I');
    vowels.add('O');
    vowels.add('U');
    
    // Or we can just use one string: "aeiouAEIOU"
    
    char[] lst = s.toCharArray();
    int left = 0, right = lst.length - 1;
    char temp;
    while (left <= right) {
      
      if (!vowels.contains(lst[left])) {
        left ++;
      }
      else {
        temp = lst[left];
        if (!vowels.contains(lst[right])) {
          right --;
        }
        else {
          lst[left] = lst[right];
          lst[right] = temp;
          left ++; // left go first
          right --;
        }
      }  
    }
    
    return new String(lst);
  }
  
  public static void main(String[] args) {
    System.out.println(reverseVowels("leetcode"));
    ArrayList<Character> lst = new ArrayList<>();
    lst.add('a');
    lst.add('e');
    lst.add('o');
    System.out.println(lst.contains('o'));
  }

}
