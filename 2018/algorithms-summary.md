
## Summary

#### 1. Two Sum (array, hash table)

- My solution

Wrong attempt: iterate through the array, calculate the `diff` between `target` and current value, if  `diff` in the array, return current index and `diff`'s index. Failed case: `num = [3,2,4], target = 6`, `num = [3,3], target = 6`.

AC: iterate through the array, calculate the `diff`, at same time create a dictionary to map value to index; check if `diff` is in the map, if yes, return the current index and `diff`'s index. Update the dictionary should behind the `if` statement, since the duplicate key will change the index (index of `diff`).

- Public solution

Brute force: iterate through the array, and search the `diff` in the rest array use a `for` loop.

Hash table: 1) need a more efficient way to check if `diff` in the array, use hash table to improve - first iterate through the array and create the hash table, then iterate the array again check if `diff` is in the hash table, where `diff`'s index cannot equal to current value index; 2) same with my AC solution.

#### 9. Palindrome Number (math)

- My solution

Use two pointers.

- Public solution

Use divide and mode operation to get the half of the number.

#### 21. Merge Two Sorted Lists (linked list)

- My solution

Wrong attempt: create a `merged` node, head is first smaller value of `l1` and `l2`, a `temp` node to be updated, use `while` loop - when `l1.next` or `l2.next` is not empty, keep update, then append the rest of `l1` or `l2` (at least one will only have one node left). Failed case: `l1 = [2], l2 = [1]` both have only one value, `l1 = [-9, 3], l2 = [5, 7]` one is strictly smaller than the other.

AC: create a `merged` node with `None` head, a `temp` node with `None` head; `merged.next` should be the output, `temp` is the node to be updated. Use `while` loop - when `l1` and `l2` are not empty, keep update, then append the rest of `l1` or `l2` (at most one will only have one node left). 

- Public solution

Recursion (super).

#### 26. Remove Duplicates from Sorted Array (array, two pointers)

- My solution

Two pointers.

#### 27. Remove Element (array, two pointers)

- My solution

Two pointers (start at `-1`), the rest idea is same as #26.

- Public solution

Also use two pointers, but more efficient when removed element are rare: when detect the removed element, swap it with the last element, then reduce the array size by 1.

#### 28. Implement strStr() (two pointers, string)

- My solution

Two pointers, no magic logic, careful about the update of the pointers (no plus one, but need to move back).

#### 66. Plus One (array, math)

- My solution

Use polynomial equation to get the number, use floor division and mode operation to get digits.

- Public solution

Recursion; back-ward iteration, based on whether it is 9 for the last digit.

#### 125. Valid Palindrome (two pointers, string)

- My solution

Two pointers, notice the return condition and corner case (only one alphanumeric but could have other symbols).

#### 141. Linked List Cycle (linked list, two pointers)

- My solution 

Two pointers, if the faster one is found behind the lower one, then it is cyclic. Notice to check the node is None or has next before doing next operation.

- Public Solution:

Hash table, if current node is in hash table, then it is cyclic.

#### 167. Two Sum II (array, two pointers, binary search)

- My solution

Two pointers and sorted arrays.

#### 169. Majority Element (array, bit manipulation, divide conquer)

- My solution

Sort and take the middle number.

- Public solution

Brute Force; hash table; divide conquer; Boyer-Moore Voting algorithm

#### 234. Palindrome Linked List (two pointers, linked list)

- My solution (**NO AC SOLUTION**)

Try to reverse the linked list chain, and compare the old head and new head.

- Public solution

Use two pointers: fast pointer and slow pointer, run through the linked list where **fast is twice faster than slow, then when fast is at end, slow is at the middle. Need to write a reverse function, then reverse at slow, it will return the second half of the linked list chain, then compare this with the head**.


#### 345. Reverse Vowels of A String (string, two pointers)

- My solution

Two pointers, notice upper and lower case for string.

#### 349. Intersection of Two Arrays (hash table, two pointers, binary search, sort)

- My solution

Sort two array first, then use two pointers.

#### X. Tips and Notice

- Initialize iterate variable if use `while` loop.
- Be careful when index the last element, `x[length(x)]` will be out of index.
- Be careful for pop stack, need to check whether stack is empty.
- Be careful for empty input, especially for array
- Don't forget empty input case, in this case some methods cannot be invoked.
- Add `self.` before methods in class when use recursion in Python.
- For linked list, must check itself or next is None or not.