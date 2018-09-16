/*
  https://leetcode.com/problems/sum-of-square-numbers/description/
*/

public class SumOfSquare {
  public static boolean judgeSquareSum(int c) {
    int left = 0, right = (int) Math.sqrt(c);
    boolean ans = false;
    
    // right should start from sqrt(c)
    if (right * right == c)
      return true;
    
    while (left <= right) {
      if (left * left + right * right > c) {
        right -= 1;
      }
      else if (left * left + right * right < c) {
        left += 1;
      }
      else {
        ans = true;
        break;
      }
    }
    
    return ans;
  }

  public static void main(String[] args) {
    System.out.println(judgeSquareSum(1000000));
  }
}
