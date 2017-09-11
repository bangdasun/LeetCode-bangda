/*
  https://leetcode.com/problems/merge-two-sorted-lists/description/
*/


//public class ListNode {
//  int val;
//  ListNode next;
//  ListNode(int x) {
//    val = x;
//  }
//}

public class MergeSortedList {
  
  public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    
    if (l1 == null) {
      return l2;
    }
    
    if (l2 == null) {
      return l1;
    }
    
    ListNode merged;
    if (l1.val < l2.val) {
      merged = l1;
      merged.next = mergeTwoLists(l1.next, l2);
    }
    else {
      merged = l2;
      merged.next = mergeTwoLists(l2.next, l1);
    }
    
    return merged;
  }
  
  public static void main(String[] args) {
    
    ListNode l1 = new ListNode(3);
    l1.next = new ListNode(4);
    System.out.println(l1.val); // return 3
    System.out.println(l1.next.val); // return 4
    System.out.println(l1.next.next); // return null
    
    l1.next.next = new ListNode(6);
    l1.next.next.next = new ListNode(8);
    
    ListNode l2 = new ListNode(1);
    l2.next = new ListNode(2);
    l2.next.next = new ListNode(3);
    l2.next.next.next = new ListNode(9);
    
    ListNode merged = mergeTwoLists(l1, l2);
    System.out.println(merged.val);
    System.out.println(merged.next.val);
    System.out.println(merged.next.next.val);
    System.out.println(merged.next.next.next.val);
    System.out.println(merged.next.next.next.next.val);
    System.out.println(merged.next.next.next.next.next.val);
    
    
    
  }
}
