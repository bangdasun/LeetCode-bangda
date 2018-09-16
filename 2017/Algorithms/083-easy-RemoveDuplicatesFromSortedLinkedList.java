/*
  https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
*/

import java.util.HashMap;

public class RemoveDuplicatesFromSortedLinkedList {
  public static ListNode deleteDuplicates(ListNode head) {
    
    if (head == null || head.next == null) {
      return head;
    }
    
    // The remove process is same as RemoveLinkedListElements
    HashMap<Integer, Integer> map = new HashMap<>();
    ListNode pseudo_head = new ListNode(-1);
    pseudo_head.next = head;
    ListNode curr = head;
    ListNode prev = pseudo_head;
    int count = 0;
    
    while (curr != null) {
      if (!map.containsKey(curr.val)) {
        map.put(curr.val, count);
        count += 1;
        prev = prev.next;
      } 
      else {
        prev.next = curr.next;
      }
      curr = curr.next;
    }
    
    return pseudo_head.next;
  }
  
  // more straightforward method: make good use of "sorted"
  // https://leetcode.com/problems/remove-duplicates-from-sorted-list/solution/
  
  public static void main(String[] args) {
    ListNode head = new ListNode(2);
    head.next = new ListNode(2);
    
    head = deleteDuplicates(head);
    System.out.println(head.val);
    System.out.println(head.next);
    //System.out.println(head.next.val);
    //System.out.println(head.next.next.val);
    //System.out.println(head.next.next.next.val);  
  }
 
}
