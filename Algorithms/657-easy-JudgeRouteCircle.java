/*
  https://leetcode.com/problems/judge-route-circle/description/
*/

public class JudgeRouteCircle {
  public static boolean judgeCircle(String moves) {
    
    if (moves.equals(""))
      return false;
    
    int num_l = 0, num_r = 0, num_u = 0, num_d = 0;
    
    for (int i = 0; i < moves.length(); i++) {
      if (moves.charAt(i) == 'R')
        num_r ++;
      else if (moves.charAt(i) == 'L')
        num_l ++;
      else if (moves.charAt(i) == 'U')
        num_u ++;
      else
        num_d ++;
    }
    
    if (num_l == num_r && num_u == num_d)
      return true;
    else
      return false;
    
  }
  
  public static void main(String[] args) {
    System.out.println(judgeCircle("LL"));
    System.out.println(judgeCircle(""));
  }

}
