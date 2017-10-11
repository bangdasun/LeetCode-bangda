/*
  https://leetcode.com/problems/count-primes/description/
*/

import java.util.HashMap;

public class CountPrimes {
  
  // Time limit exceed...
  public static boolean isPrime(int n) {
    HashMap<Integer, Integer> map = new HashMap<>();
    
    if (n < 2) 
      return false;
    
    for (int i = 2; i < n; i++) {
      map.put(i, i);
    }
    
    for (int i = 2; i < n; i++) {
      int d = n / map.get(i);
      if (map.containsKey(d) && d * map.get(i) == n) {
        return false;
      }
    }
    
    return true;
  }
  
  public static int countPrimes(int n) {
    int count = 0;
    for (int i = 2; i < n; i++) {
      if (isPrime(i)) {
        count ++;
      }
    }
    
    return count;
  }
  
  // Faster method
  public static int countPrimes2(int n) {
    boolean[] notPrime = new boolean[n];
    int count = 0;
    for (int i = 2; i < n; i++) {
      if (!notPrime[i]) {
        count ++;
        for (int j = 2; i * j < n; j++) {
          notPrime[i * j] = true;
        }
      }
    }
    
    return count;
  }
  
  public static void main(String[] args) {
    System.out.println(isPrime(2));
    System.out.println(isPrime(3));
    System.out.println(isPrime(4));
    System.out.println(isPrime(5));
    System.out.println(isPrime(7));
    
    System.out.println(countPrimes2(10000));
  }

}
