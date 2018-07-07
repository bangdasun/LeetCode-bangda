/*
  https://leetcode.com/problems/add-digits/description/
*/

public class AddDigits {
  public static int addDigits(int num) {
    
    // Theory: 1 + (num - 1) % 9
    
    if (num == 0)
      return 0;
    
    // (100a + 10b + c) % 9 = (a + b + c) % 9
    
    int ans = 0;
    ans = (num % 9 == 0) ? 9 : num % 9; // keep in mind that mod will generate non-negative
    return ans;
  }
  
  public static void main(String[] args) {
    System.out.println(addDigits(0));
  }

}
