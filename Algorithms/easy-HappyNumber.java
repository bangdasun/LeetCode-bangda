/*
  https://leetcode.com/problems/happy-number/description/
*/

import java.util.ArrayList;
import java.util.HashMap;

public class HappyNumber {
  public static boolean isHappy(int n) {
    
    if (n == 0) 
      return false;
    
    if (n == 1)
      return true;
    
    HashMap<Integer, Integer> map = new HashMap<>();
    
    int count = 0;
    
    while (true) {
      int ssq = 0;
      ArrayList<Integer> numbers = new ArrayList<>();
      
      while (n / 10 > 0) {
        numbers.add(n % 10);
        n /= 10;
      }
      numbers.add(n);
      
      for (int i = 0; i < numbers.size(); i++) {
        ssq += numbers.get(i) * numbers.get(i);
      }
      n = ssq;
      
      if ((ssq > 10 && ssq / 10 == 0) || ssq == 1)
        return true;
      
      if (!map.containsKey(ssq)) {
        
        map.put(ssq, count);
        count += 1;
      } 
      else {
        return false;
      }
    }
  }
  
  public static void main(String[] args) {
    
    for (int i = 0; i < 20; i++)
      System.out.println(isHappy(i));
  }

}
