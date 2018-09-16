/*
  https://leetcode.com/problems/palindrome-number/description/
*/

public class PalindromeNumber {
  public boolean isParlindrome(int x) {
    
    // corner case
    if (x < 0 || (x % 10 == 0 && x != 0))
      return false;
    
    // compare half of the number:
    // check x from left and set reverse_x to be right half of x
    int reverse_x = 0;
    while (x > reverse_x) {
      reverse_x = reverse_x * 10 + x % 10;
      x /= 10;
    }
    
    // if number of digits in x is odd, we will end up with like:
    // x = 12, reverse_x = 123
    return x == reverse_x || x == reverse_x / 10;
  }

}
