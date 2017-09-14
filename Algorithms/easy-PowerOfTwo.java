/*
  https://leetcode.com/problems/power-of-two/description/
*/

public class PowerOfTwo {
  public static boolean isPowerOfTwo(int n) {
    if (n == 0)
      return false;
    
    if (n == 1)
      return true;
    
    if (n % 2 == 0 && n > 1) {
       return isPowerOfTwo(n / 2);
    } else {
      return false;
    }
  }
  
  public static void main(String[] args) {
    
    for (int i = 0; i < 20; i++)
      System.out.println(isPowerOfTwo(i));
  }

}
