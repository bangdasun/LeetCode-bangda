/*
  https://leetcode.com/problems/perfect-number/description/
*/

import java.util.ArrayList;

public class PerfectNumber {
  public static boolean checkPerfect(int num) {
    
    // Theory: 28 = 2^2 * (2^3 - 1)
    
    // corner case
    if (num == 1)
      return false;
    
    int mid = (int) Math.sqrt(num);
    ArrayList<Integer> divisor = new ArrayList<>();
    
    for (int i = 2; i <= mid; i++) {
      if (num % i == 0) {
        divisor.add(i);
        divisor.add(num / i);
      }
    }
    
    divisor.add(1);
    int sum = 0;
    
    for (int i = 0; i < divisor.size(); i++) {
      sum += divisor.get(i);
    }
    
    return sum == num;
  }
  
  public static void main(String[] args) {
    System.out.println(checkPerfect(28));
    System.out.println(checkPerfect(6));
    System.out.println(checkPerfect(496));
    System.out.println(checkPerfect(0));
  }

}
