
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

Use two pointers, check if the value they point to are same during the iteration.

- Public solution

Use divide and mode operation to get the half of the number.

#### 14. Longest Common Prefix (string)

- My solution

Brute force: try to iterate through every string in `strs`, if there is a mismatch, output the current `common_prefix`.

- Public solution

Horizontal scanning: use the observation that `LCP(s1, ..., sn) = LCP(LCP(LCP(s1, s2), s3), ..., sn)`; Vertical scanning: improve the previous one if there is a very short string at the end of the array; 

**Divide Conquer** (to be continued).

#### 21. Merge Two Sorted Lists (linked list)

- My solution

Wrong attempt: create a `merged` node, head is first smaller value of `l1` and `l2`, a `temp` node to be updated, use `while` loop - when `l1.next` or `l2.next` is not empty, keep update, then append the rest of `l1` or `l2` (at least one will only have one node left). Failed case: `l1 = [2], l2 = [1]` both have only one value, `l1 = [-9, 3], l2 = [5, 7]` one is strictly smaller than the other.

AC: create a `merged` node with `None` head, a `temp` node with `None` head; `merged.next` should be the output, `temp` is the node to be updated. Use `while` loop - when `l1` and `l2` are not empty, keep update, then append the rest of `l1` or `l2` (at most one will only have one node left). 

- Public solution

Recursion (super).

#### 26. Remove Duplicates from Sorted Array (array, two pointers)

- My solution

Two pointers, one is used to be as a remark, where the number before it are all distinct, the other one is used to iterate through the array.

#### 27. Remove Element (array, two pointers)

- My solution

Two pointers (start at `-1`), the rest idea is same as #26.

- Public solution

Also use two pointers, but more efficient when removed element are rare: when detect the removed element, swap it with the last element, then reduce the array size by 1.

#### 28. Implement strStr() (two pointers, string)

- My solution

Two pointers, no magic logic, careful about the update of the pointers (no plus one, but need to move back), one pointer is use to store the position, the other is used to iterate through the whole string.

#### 35. Search Insert Position (array, binary search)

- My solution

Binary search: check the middle point in the range of `[1, len(nums)//2]` and update the bound with middle value, use `while` loop, when `left > right` it will jump out, then check the current value at `,` with `target`, if smaller than `target`, put at `m`; else put at `m+1`.

#### 58. Length of Last Word (string)

- My solution

Find the position of last space, and index the string towards to that position, then split by space and return the length of the last string.

- Public

Iterate from tail to head, if the current letter is not space, add 1 to the length ()  and continue; else if got a non-ending space (a new space), break the loop, finally return length.

#### 66. Plus One (array, math)

- My solution

Use polynomial equation to get the number, use floor division and mode operation to get digits.

- Public solution

Recursion; back-ward iteration, based on whether it is 9 for the last digit.

#### 67. Add Binary (math, string)

- My solution

Brute force: convert to decimal, get the sum and convert back to binary

- Public solution

String addition: based on addition rule, in binary case - if two digits sum larger than 2, need to increase, then set a `carry` to be 1 and put 0 at current position, if the next two digits and `carry` sum still larger than 2, put 1 at current position and `carry` is still 1, only two digits and `carry` sum smaller than 2, put the sum at current position and reset `carry` to be 0.

#### 69. Sqrt(x) (math, binary search)

- My solution (**NO AC SOLUTION**)

Try to iterate through from 0 to `int(x/2) + 1`, check whether `i*i` is larger or smaller than `x`. But take too long for large number

- Public solution

Binary search: check the middle point in the range of `[1, x//2]` and update the bound with middle value.

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

Two pointers and sorted arrays; Binary search, iterate through the array, do a binary search in range `[i+1, n-1]`.

#### 169. Majority Element (array, bit manipulation, divide conquer)

- My solution

Sort and take the middle number, since majority number is at least take half count.

- Public solution

Brute Force; hash table; divide conquer; Boyer-Moore Voting algorithm

#### 202. Happy Number (hash table, math)

- My solution

Hash table, calculate the sum square of the digits and store as key in hash table, if sum square is 1, return True, else if sum square is in the hash table key, return False, otherwise keep running (update number and reset sum square).

- Public solution

Math property:

Recursion: 1 and 4 are base case.

#### 204. Count Primes (math, hash table)

- My solution (**NO AC SOLUTION**)

Use a `isPrime()` function, then iterate through the list for `i` from 1 to `n`, remove the division from the list if `i` is not prime. Time limit exceed since it's `O(n^2)`.

- Public solution

Array: First assume all are prime, then update them since prime number cannot be divided by any number between 1 and itself. Use a array `isPrime` and each element correspond one number in `[0, n-1]`, initialize all as `True`, next start iterate from 2, if the value is `True`, then update all position at `j` times of it to be `False`; use a `count` to count the number of value to be `True`.

Hash table: **NA**.

#### 219. Contains Duplicate II (array, hash table)

- My solution

Hash table, store the value of array as key and index as value, if there is a duplicate value, check the difference between current index and value in the hash table, if less or equal to `k` then return `True`; return `False` in the end. 

#### 225. Implement Stack using Queues (stack, design)

- My solution

Wrong attempt: use one queue, `push()` need to `dequeue()` element, then put it back after append the new element. Only consider a 2 elements case, doesn't work if there are 3 elements.

AC: use two queue, either one will be empty. `push()` need to put the new element into the empty queue, then `dequeue()` all elements of the non-empty queue and append them to the empty queue (new value already appended).

- Public solution

Two queues: opposite to my solution, the `pop()` takes `O(n)` and `push()` takes `O(1)`. When `pop()`, `dequeue()` all elements except the last one to the other queue, then `dequeue()` the last element.

One queue: the `pop()` takes `O(1)` and `push()` takes `O(n)`. When `push()`, `dequeue()` all elements except the last one, each `dequeue()` is followed by `enqueue()`, then the original last element will be at the top of the 'stack'.


#### 232. Implement Queue using Stacks (stack, design)

- My solution

Wrong attempt: use two stacks, `dequeue()` need to `pop()` all elements except the first one from the non-empty stack, the first one will be the return.

AC: based on the wrong attempt, remember to `push()` back all elements in non-empty stack to the empty stack.

- Public solution

Two stacks 1: opposite to my solution, the `dequeue()` takes `O(1)` and `enqueue()` takes `O(n)`. **QUESTIONABLE**.

Two stacks 2: similar with my AC, but when `dequeue()`, also `push()` the last element into the other stack, then `pop()`.

#### 234. Palindrome Linked List (two pointers, linked list)

- My solution (**NO AC SOLUTION**)

Try to reverse the linked list chain, and compare the old head and new head.

- Public solution

Use two pointers: fast pointer and slow pointer, run through the linked list where **fast is twice faster than slow, then when fast is at end, slow is at the middle. Need to write a reverse function, then reverse at slow, it will return the second half of the linked list chain, then compare this with the head**.

#### 258. Add Digits (math)

- My solution

Brute Force, iterate until the output is less than 10.

- Public solution

Math property: `a * (10 ** n) % 9 == a % 9`, therefore just need to clarify difference cases for `a%9`. (Very **SMART** solution)

#### 268. Missing Number (math)

- My solution

The length `n` array is expected to be the array with one element removed from 0 to `n`, which the sum should be `(0+n)(n+1)/2`, the missing number is the difference of the theoretical sum and actual sum.

- Public solution

Sorting; Hash table.

#### 278. First Bad Version (binary search)

- My solution

Binary search: but the range setting and terminate condition are a little tricky: since we can only see binary feedback, therefore it's possible `m` is the first bad version, then `right` should be `m` rather then `m-1`;   
when `left` and `right` meet it will be the first bad version, we could simply check this by a size 2 input, and notice it is not necessary to be `m` now since `m` is from previous `left` and `right`.

#### 290. Word Pattern (hash table)

- My solution

Hash table, create a bijection map between `pattern` and `str`, notice that key and value are both distinct.

#### 344. Reverse String (two pointers, string)

- My solution

Two pointers, swap the value they point to.

#### 345. Reverse Vowels of A String (string, two pointers)

- My solution

Two pointers, swap the value they point to if value is in vowels, notice upper and lower case for string.

#### 349. Intersection of Two Arrays (hash table, two pointers, binary search, sort)

- My solution

Sort two array first, then use two pointers, put the smaller one into output and move to next.

#### 350. Intersection of Two Arrays II (hash table, two pointers, binary search, sort)

- My solution

Same as #349; hash table: iterate through one array and store the value count in a hash table, then iterate through another one, if the value is in the hash table, reduce the count by 1 and this value is in the intersect.

#### 374. Guess Number Higher or Lower (binary search)

- My solution

Binary search, find the position of number, similar with #35.


#### 383. Ransom Note (string)

- My solution

Hash table: the count of distinct letters in Ransom Note should be less or equal to magazine.

- Public solution

Use `set()` and `count()` if use Python, no hash table needed, just iterate through distinct letters in Ransom Note and compare the letter count.

#### 387. First Unique Character in a String (hash table, string)

- My solution

Hash table, store the count of the letter, then iterate through the string, whenever find the letter has value to be 1 in the hash table, return the index. Finally return -1.



#### 657. Robot Return to Origin (string)

- My solution

Move count: the left - right, up - down counts should be symmetric.

Coordinates calculate: the final coordinates are same with initial coordinates.

#### 771. Jewels and Stones (hash table)

- My solution

Hash table, store the count of letters in `S` in the hash table and add the count which the key is in `J`.

#### X. Tips and Notice

- Initialize iterate variable if use `while` loop.
- Be careful when index the last element, `x[length(x)]` will be out of index.
- Be careful for pop stack, need to check whether stack is empty.
- Be careful for empty input, especially for array
- Don't forget empty input case, in this case some methods cannot be invoked.
- Add `self.` before methods in class when use recursion in Python.
- For linked list, must check itself or next is None or not.
- Be careful for the condition in `while` loop.