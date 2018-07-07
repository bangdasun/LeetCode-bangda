/*
  https://leetcode.com/problems/delete-node-in-a-linked-list/description/  
*/

public class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
    val = x;
  }
}


public class DeleteNodeInLinkedList {
  public static void deleteNode(ListNode node) {
    node.val = node.next.val;
    node.next = node.next.next;
  }
  
  public static void main(String[] args) {
    ListNode head = new ListNode(3);
    head.next = new ListNode(4);
    head.next.next = new ListNode(5);
    head.next.next.next = new ListNode(6);
    
    deleteNode(head.next);
    System.out.println(head.val);
    System.out.println(head.next.val);
    System.out.println(head.next.next.val);
  }
}