/*
  https://leetcode.com/problems/reverse-string/description/
*/

public class ReverseString {
  
  // Naive solution
  public static String reverseString(String s) {
    
    String[] str_list= s.split("");
    String reverse_s = "";
    for (int i = str_list.length - 1; i >= 0; i--) {
      reverse_s = reverse_s.concat(str_list[i]);
    }
    
    return reverse_s;
  }
  
  public static String reverseString2(String s) {
    
    // Just need to reverse first half and second half
    char[] char_lst = s.toCharArray();
    int left = 0, right = char_lst.length - 1;
    
    while (left < right) {
      char temp = char_lst[left];
      char_lst[left] = char_lst[right];
      char_lst[right] = temp;
      left ++;
      right --;
    }
    
    return new String(char_lst);
  }
  
  public static void main(String[] args) {
    String reverse_s = reverseString2("hello");
    System.out.println(reverse_s);
    //for (String str: reverse_s) {
    //  System.out.println(str);
    //}
    
    //System.out.println("hello".concat("o"));
  }
}
