/*
  https://leetcode.com/problems/top-k-frequent-elements/description/
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

// Use idea of bucket sort or heap
public class TopKFrequentElements {
  public static List<Integer> topKFrequent(int[] nums, int k) {
    List<Integer>[] bucket = new List[nums.length + 1];
    HashMap<Integer, Integer> map = new HashMap<>();
    
    // Frequency table
    for (int i = 0; i < nums.length; i++) {
      if (!map.containsKey(nums[i])) {
        map.put(nums[i], 0);
      }
      else {
        map.put(nums[i], map.get(nums[i]) + 1);
      }
    }
    
    // Iterate through the key
    for (int key: map.keySet()) {
      
      int freq = map.get(key);
      
      // position is frequency
      if (bucket[freq] == null) {
        bucket[freq] = new ArrayList<>();
      }
      bucket[freq].add(key);
    }
    
    List<Integer> output = new ArrayList<>();
    
    // Start from high frequency
    for (int i = bucket.length - 1; i >= 0 && output.size() < k; i--) {
      if (bucket[i] != null) {
        output.addAll(bucket[i]);
      }
    }
    
    return output;
  }
  
  public static void main(String[] args) {
    int[] nums = {1, 1, 1, 2, 2, 3, 3, 3, 3};
    List<Integer> output = topKFrequent(nums, 2);
     
    for (int i = 0; i < output.size(); i++) {
      System.out.println(output.get(i));
    }
  }

}
