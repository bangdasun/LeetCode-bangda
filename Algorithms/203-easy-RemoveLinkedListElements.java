/*
  https://leetcode.com/problems/remove-linked-list-elements/description/
*/

public class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
  }
}


public class RemoveLinkedListElements {
  
  // This solution cannot pass the case that there are only the head and delete it
  public static ListNode removeElements(ListNode head, int val) {
    ListNode curr = head;
    ListNode prev = null;
    
    while (curr != null) {
      if (curr.val != val) {
        prev = curr;
        curr = curr.next;
      } 
      else {
        curr = curr.next;
        prev.next = curr;
      }
    }
    
    return head;
  }
  
  public static ListNode removeElements2(ListNode head, int val) {
    
    ListNode pseudo_head = new ListNode(-1);
    pseudo_head.next = head;
    
    ListNode curr = head;
    ListNode prev = pseudo_head;
    
    while (curr != null) {
      if (curr.val != val) {
        prev = prev.next; 
      } 
      else {
        prev.next = curr.next; // skip curr
      }
      
      curr = curr.next;
    }
    
    return pseudo_head.next; // not head
  }
  
  public static void main(String[] args) {
    ListNode head = new ListNode(3);
    //head.next = new ListNode(4);
    //head.next.next = new ListNode(6);
    //head.next.next.next = new ListNode(4);
    //head.next.next.next.next = new ListNode(5);
    
    
    head = removeElements2(head, 3);
    System.out.println(head);
    //System.out.println(head.next.val);
    //System.out.println(head.next.next.val);
    
  }
}
