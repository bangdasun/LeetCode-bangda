/*
  https://leetcode.com/problems/reverse-linked-list/description/
*/

public class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
  }
}


public class ReverseLinkedList {
  
  // non-recursive
  public static ListNode reverseList1(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    
    /*
     * the goal at each iteration is let curr -> prev
     * therefore we need to store prev node beforehead
     * we also need to store the next node before changing reference
     * */
    while (curr != null) {
      ListNode temp = curr.next;
      curr.next = prev; // change reference: curr -> prev, not set prev to be current.next
      // update, like i++ step
      prev = curr;
      curr = temp;
    }
    
    return prev;
  }
  
  // recursive
  public static ListNode reverseList2(ListNode head) {
    
    if (head == null || head.next == null) 
      return head;
    
    ListNode new_head = reverseList2(head.next);
    head.next.next = head;
    head.next = null;
    return new_head;
  }
  
  public static void main(String[] args) {
    ListNode head = new ListNode(4);
    head.next = new ListNode(5);
    head.next.next = new ListNode(6);
    head.next.next.next = new ListNode(7);
    head.next.next.next.next = new ListNode(8);
    
    //ListNode newhead = reverseList1(head);
    ListNode newhead = reverseList2(head);
    
    System.out.println(newhead.val);
    System.out.println(newhead.next.val);
    System.out.println(newhead.next.next.val);
    System.out.println(newhead.next.next.next.val);
    
  }

}
