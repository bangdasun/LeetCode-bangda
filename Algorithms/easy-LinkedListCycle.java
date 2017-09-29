/*
  https://leetcode.com/problems/linked-list-cycle/description/
*/

import java.util.HashSet;

public class LinkedListCycle {
  public static boolean hasCycle(ListNode head) {
    HashSet<ListNode> visited = new HashSet<>();
    
    while (head != null) {
      if (visited.contains(head)) {
        return true;
      }
      else {
        visited.add(head);
      }
      head = head.next;
    }
    
    return false;
  }
  
  // For O(1) space, use two pointers: slower and faster
  // https://leetcode.com/problems/linked-list-cycle/solution/
  
  public static void main(String[] args) {
    
  }

}
