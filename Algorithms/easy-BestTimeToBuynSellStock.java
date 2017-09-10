
public class BestTimeToBuynSellStock {
  public static int maxProfit(int[] prices) {
    
    int left = 0, right = prices.length - 1;
    int profit = 0;
    
    // notice for empty array
    if (right + 1 > 0)  
      profit = Math.max(prices[right] - prices[left], 0);
   
    while (left < right) {
      if (prices[right] - prices[left + 1] > prices[right - 1] - prices[left]) {
        profit = Math.max(profit, prices[right] - prices[left + 1]);
        left ++;
      }
      else {
        profit = Math.max(profit, prices[right - 1] - prices[left]);
        right --;
      }
    }
    
    return profit;
  } // BUT THIS APPROACH FAILS TO DEAL WITH EQUAL PRICE CASE!
  // Try not to use two pointers in searching array without order
  
  
  // Again we can apply Kadane's algorithm
  public static int maxProfit2(int[] prices) {
    int current_max = 0, profit = 0;
    
    for (int i = 1; i < prices.length; i++) {
      current_max = Math.max(0, current_max += prices[i] - prices[i - 1]);
      profit = Math.max(current_max, profit);
    }
    
    return profit;
  }
  
  public static void main(String[] args) {
    // int[] prices = {};
    // int[] prices = {7, 6, 4, 3, 1};
    int[] prices = {2, 1, 2, 1, 0, 1, 2};
    System.out.println(maxProfit2(prices));
    //System.out.println(prices.length);
  }
}
