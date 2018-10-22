
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

#### 53. Maximum Subarray (array, dynamic programming, divide conquer)

- My solution (**NO AC SOLUTION**)

Cumulative sum: get the cumulative sum of the array. The maximum subarray is the array has maximum difference in the cumulative sum array.

- Public solution

Dynamic programming 1 (Kadane's algorithm): if we know the maximum subarray sum end at position `i`, what is the maximum subarray sum end at `i + 1`? The answer is either the maximum subarray sum end at `i + 1`, or it doesn't. That's say, if the maximum subarray sum end at `i` is larger than 0, we should add `nums[i + 1]` into it, that gives the maximum subarray sum at `i + 1` is `max(nums[i + 1], nums[i + 1] + max_sum_end)`. Then we need to find the maximum value of it.

Dynamic programming 2: if the previous element is larger than 0, current element is equal to current element + previous element; else the previous element is less or equal to 0, then ignore it, current element stay the same.


#### 58. Length of Last Word (string)

- My solution

Find the position of last space, and index the string towards to that position, then split by space and return the length of the last string.

- Public solution

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

#### 70. Climbing Stairs (dynamic programming)

- My solution

Dynamic programming: current solution is from previous solution: `S(n) = S(n - 1) + S(n - 2)`.

- Public solution

Recursion with memorization: **TO BE CONTINUED**.

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

#### 189. Rotate Array (array)

- My solution

Sliding array: increase the array multiple times (`k // n + 1`), then slicing last `k` to last `k + n`.

- Public solution

Reverse: reverse the whole list, then reverse the first `k` and last `k - n`.

Extra array: use an extra array, the number at index `i` in the original array is placed at `i + k` right now. There is a trick use mod operation: `a[(i + k) % n] = nums[i]`.

Cyclic Replacements: **TO BE CONTINUED**.


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

#### 217. Contains Duplicate (array, hash table)

- My solution

Hash table: if the value in hash table keys, then return True; else add the value as key and store value 1. Return False in the end.

- Public solution

Sorting: same number will be consecutive.


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

#### 268. Missing Number (array, math)

- My solution

The length `n` array is expected to be the array with one element removed from 0 to `n`, which the sum should be `(0+n)(n+1)/2`, the missing number is the difference of the theoretical sum and actual sum.

- Public solution

Sorting; Hash table; Bit manipulation.

#### 278. First Bad Version (binary search)

- My solution

Binary search: but the range setting and terminate condition are a little tricky: since we can only see binary feedback, therefore it's possible `m` is the first bad version, then `right` should be `m` rather then `m-1`;   
when `left` and `right` meet it will be the first bad version, we could simply check this by a size 2 input, and notice it is not necessary to be `m` now since `m` is from previous `left` and `right`.

#### 283. Move Zeros (array, two pointers)

- My solution

Brute force: similar with bubble sort, if there is a zero, swap it with next non-zero elements.

- Public solution

Linear scan: save the `lastNonZeroIdx`, add non-zero values from beginning (`lastNonZeroIdx` initialized as 0), then assign 0 to the rest array (start from latest `lastNonZeroIdx`).

Two pointers: set `curr` and `lastNonZeroIdx`, swap `lastNonZeroIdx` and `curr` values if `curr` is at non-zero values.


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

#### 367. Valid Perfect Square (binary search)

- My solution

Binary search, find if there is a number in `[0, num // 2]` squared to be equal to `num`.

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

#### 389. Find the Difference (hash table, bit manipulation)

- My solution

Wrong attempt: build a hash table based on `s`, then iterate through `t` to check if every letter is in the hash table. But it's possible that the extra letter is a duplicate letter in `s`.

AC: same methods, but save the value of hash table as count, if letter in `t` also in hash table, check the count is larger than 0: if yes, reduce the count by 1, if no, then this is the extra letter.

#### 409. Longest Palindrome (hash table)

- My solution:

Wrong attempt: build a hash table based on `s` with key to be letter and value to be the count, then iterate through the hash table, if the value is even, add it, else if the value is odd and larger than 1, reduce it by 1 and add it, else if the value is 1, remark it. Then finally if the "is there any 1" remark is `True`, add the length by 1. But this doesn't consider when there is only one odd number and it's larger than 1, corner case: `ccc`.

AC: same method, but also add a remark: if there is a odd number larger than 1. Finally add length by 1 if either one of the remarks is `True`. 

- Public solution:

Hash table: build a hash table based on count, iterate through and add by `(value // 2) * 2` each time. Then if there is a odd number, and the length is still even, increase the length by 1. (This will happen when meet the first odd number, second one the length is odd not even).

#### 434. Number of Segments in a String (string)

- My solution

Linear scan: iterate through the string, and set 2 state variable `is_space` and `is_non_space` to indicate whether current pointer is in space characters or non space characters. If the state change from space (or at the beginning) to non space, add the count by 1. Return the count in the end.

- Public solution

Linear scan: same idea, but more clear - just find the first character of each segment (from beginning or from space), and update the count.

#### 441. Arranging Coins (math, binary search)

- My solution

Math: the sum of `1+2+3+...+n` is `n * (n + 1) / 2`, then the answer `n` should satisfied `n * (n + 1) / 2 <= target < (n + 1) * (n + 2) / 2`.

- Public solution

**TO BE CONTINUED**.

#### 557. Reverse Words in a String III (string)

- My solution

Split the string by space and put all words in the array, then reverse each word in the array, and concatenate them separated by space

#### 581. Shortest Unsorted Continous Subarray (array)

- My solution

Sorting: make a copy of `nums` and sort it. Then compare two arrays using 2 loops, first loop is to mark the leftmost mis-match position, which is the start of the subarray; second loop is to mark the rightmost mist-match position, which is the end of the subarray. The length will be `end - start + 1`.

- Public solution

**TO BE CONTINUED**.


#### 599. Minimum Index Sum of Two Lists (hash table)

- My solution

Hash table, build a hash table based on shorter list, key is the name and value is index, define `curr_min` as current min sum of index (initialized as sum of length), and output initialized as a empty list; then iterate through another list, if the value is in hash table keys, compare sum of index with `curr_min`, if it is smaller or equal to `curr_min`, append it to the output. Finally return the output.

- Public solution

No hash table: traverse over the various sum of index and determine if any such string exists in list 1 and list 2 such that the sum of its indices in the two lists equals sum (index could be negative, say it is invalid).

Hash table: for every value in one list, search it in another list, if there is a match, store it into the hash table as key to be the sum of index and value to be the list of corresponding values.

#### 605. Can Place Flowers (array)

- My solution

Min array: create `left` and `right` to store the closest non-empty position for each position. Then count the number of values larger than 1 with group by 0.

- Public solution

Simple scan: simply iterate through the array, if there the adjacent places are both empty, place it 1. Where the head and tail positions just need to check one place. The logic is a little tricky.

#### 643. Maximum Average Subarray I (array)

- My solution (**NO AC SOLUTION**)

Brute force: calculate the sum of the sliding window, and update the maximum if current maximum is larger than record maximum. But take too long to run long list.

- Public solution

Cumulative sum: create a `cumsum` array, then the difference of `i`th value and `i+k`th value of the array is exactly the sum of subarray in the raw array. The difference is initialized as `k`th value in the `cumsum` array. 

Brute force (same as my sliding window): but use smarter method, just update the current maximum by add the difference of value to be removed and to be added.

#### 657. Robot Return to Origin (string)

- My solution

Move count: the left - right, up - down counts should be symmetric.

Coordinates calculate: the final coordinates are same with initial coordinates.

#### 674. Longest Continuous Increasing Subsequence (array)

- My solution

Except the zero-length array, the smallest return will be 1, so initialize `cnt` and `curr_max` as 1, then iterate through the array start at index 1, calculate the difference of values at current index and previous index, if the difference is greater than 0, increase the `cnt` by 1, else reset it as 1, finally update the `curr_max` to be `max(curr_max, cnt)`, and return it when iteration terminates.

- Public solution

Sliding window: every continuous increasing subarray is disjoint, mark the position when `nums[i - 1] >= nums[i]`, store `i` in variable `anchor`, record a candidate answer of `i - anchor + 1`.

#### 680. Valid Palindrome II (string)

- My solution (**NO AC SOLUTION**)

Two pointers, go from head (`i`) and tail (`j`), if there is a mismatch, mark `delete_one` to be True, then move `i` or `j` based on checking `s[i + 1] == s[j]` or `s[i] == s[j - 1]`. But it's possible that both condition will satisfied, then no decision can be made.

- Public solution

Greedy algorithm: still begin with two pointers, if `s[i] != s[j]` then check whether `s[i + 1]` to `s[j]` or `s[i]` to `s[j - 1]` is palindrome, either one is palindrome then return True; else if `s[i] == s[j]`, update the pointers.

#### 686. Repeated String Match (string)

- My solution

Brute force: check if `B` is in `A * k`, where `k` will be the output. The edge condition is `len(B)` is half of `len(A)`.

- Public solution

Ad-hoc: same with my idea. But calculate `q` then `len(B) <= len(A * q)`. `q = (len(B) - 1) // len(A) + 1`, and if the answer is not -1, then `B` must be in `A * q` or `A * (q + 1)`.

#### 697. Degree of an Array (array)

- My solution (**NO AC SOLUTION**)

Find the degree of the array at first (use hash table), also save the value with frequency equal to degree, then for each value, find the leftmost and rightmost position in `nums`, find the minimum difference. But takes too long to run.

- Public solution

Two pointers (dictionary): define `slow` and `fast` hash table, `slow` is to record leftmost positions of all elements in array, `fast` is to record rightmost positions of all elements in array, then store the number and count in `dct` hash table. Next find the maximum value in `dct`, then for corresponding key (corresponding to key in `slow` and `fast`), calculate the minimum differences (`fast[k] - slow[k] + 1`).

#### 704. Binary Search (binary search)

- My solution

Binary search.

#### 709. To Lower Case (string)

- My solution

Hash table: build a hash table to map from upper case to lower case, then convert the string to list, iterate through the list and do the replacement if necessary, finally convert the list back to string.

#### 724. Find Pivot Index (array)

- My solution (**NO AC SOLUTION**)

Cumulative sum: calculate left and right cumulative sum of the array, then iterate through two cumsum array, if there is a match, check whether they are valid (pivot index exist). But cannot deal with 0 answer case. (other corner case include: cumsum array is not monotonic increase, could decrease)

- Public solution

Prefix sum: calculate the left cumulative sum, and check if it equals right cumulative sum without value at current index. Need to calculate the sum of the array at first.

#### 771. Jewels and Stones (hash table)

- My solution

Hash table: store the count of letters in `S` in the hash table and add the count which the key is in `J`.

#### 796. Rotate String (string)

- My solution

Brute force: remove the first value and append it at end for `A`, check if it equals `B` in each iteration.

- Public solution

Simple check: check if `B` is the subset of `A + A`.

Rolling hash: **TO BE CONTINUED**.

KMP algorithm: **TO BE CONTINUED**.

#### 804. Unique Morse Code Words (string)

- My solution

Hash table: build a map between letters and codes. Then for each letter in each word in the list, store the transformed codes in a list, finally count the number of unique transformed codes in the list.

#### 821. Shortest Distance to a Character (array)

- My solution

Brute Force: first save the location of `C`. Then initialize a distance array with value to be the length of the array, iterate through this array, calculate the minimum distance to all location of `C` and save it as distance. Finally return the distance array.

- Public solution

Min array: for each index, find the distance to the next `C` going left and right, the distance is the minimum of these two values. When going left to right, save the last `C` location as `prev`, the distance is `i - prev`; when going right to left, save the last `C` location as `prev`, the distance is `prev - i`. Finally take the minimum of these two answers to create the final distance array.

#### 830. Positions of Large Groups (array)

- My solution

Two pointers: `i` and `j` start at 0, keep increase `j` until `S[i] != S[j]`, then check the difference (length of the group) and `i` start at `j`. Corner case: `aaa` at end, here `j` will not move out of the last `a`, therefore need a extra check after the loop. 

#### 832. Flipping an Image (array)

- My solution

Brute Force.

#### 836. Rectangle Overlap (math)

- My solution

Check position: check the position of: upper right of rec 1 and lower left of rec 2, upper left of rec 1 and lower right of rec 2, lower right of rec 1 and upper left rec 2, lower left of rec 1 and upper right rec 2. The relation should be `and`, since once 1 condition is not satisfied, they will not overlap.

- Public solution

Check position: more precise solution.

Check area: if overlap, there must be a rectangle where both dimensions are position: whether two line segments overlap. For example: if `min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])`, there will be a horizontal overlap.

#### 844. Backspace String Compare (two pointers, stack)

- My solution

Stack: create two empty stacks, iterate through two strings simultaneously, if there is a `#` and the stack is not empty, pop it; if not `#`, append it to the stack. When iterate terminate, it's possible that one string is not complete, then use the same step to finish scanning. Finally compare if two stacks are equal.

- Public solution

String builder: same as stack solution.

Two pointers: **TO BE CONTINUED**.

#### 849. Maximum Distance to Closest Person (array)

- My solution (**NO AC SOLUTION**)

Two array: use two array to store the leftmost position of 0's and rightmost position of 0's. Then the difference of two arrays will be the length of 0's part. But this cannot deal with lead 0's. Corner case is complicate to deal with.

- Public solution

Next array: Let `left[i]` to be the distance of seat `i` to the closest person sitting to left of `i`, same with `right[i]`. Then the distance to closest person when seating at `i` is `min(left[i], right[i])`. The `max(min(left[i], right[i]))` is the answer.

Two Pointers: **TO BE CONTINUED**

#### 852. Peak Index in a Mountain Array (array)

- My solution

Linear scan: the first position that `A[i] > A[i + 1]` is the answer.

- Public solution

Binary search: find the first position that `A[i] > A[i + 1]`.

#### 859. Buddy Strings (string)

- My solution (**NO AC SOLUTION**)

Brute force: enumerate all pairs of values in `A`, swap them and check if it could get `B`, if not, need to be swap back. But takes too long to run.

- Public solution

Enumerate cases: if the result is True, then `A` and `B` only have two unmatched positions when `A[i] == B[j]`, `A[j] == B[i]` and `A[i] != A[j]` or `A == B` which means `A[i] == A[j]`. 


#### 867. Transpose Matrix (array)

- My solution

Use matrix transpose definition `A_T[j][i] = A[i][j]`.

#### 876. Middle of the Linked List (linked list)

- My solution

Two pointers: same with #234. Use `slow` and `fast`, when `fast` is at the end, `slow` is exactly at the middle.

#### 884. Uncommon Words from Two Sentences (hash table)

- My solution

Hash table: build two hash tables where key is word and value is count, then iterate through both of them, when `cnt == 1` and the word is not in another hash table, add this word to output.

- Public solution

Hash table: could merge into one hash table and just return the word with `cnt == 1`.

#### 888. Fair Candy Swap (array)

- My solution (**NO AC SOLUTION**)

Similar to #1 Two Sum. The final size is `(sum(A) + sum(B)) / 2`. Then we just need to find `i` in `A` and `j` in `B` such that `sum(A) - i + j == (sum(A) + sum(B)) / 2`. But get TLE.

- Public solution

Use `j == i + (sum_B - sum_A) / 2` to search if `j` in `set(B)`, still get TLE if `set()` is not used.

#### 896. Monotonic Array (array)

- My solution

Wrong attempt: iterate through array, use binary number to represent whether it's increasing or decreasing, then the sum of binary number should be either 0 or array size - 1. But binary representation cannot deal with equal case.

AC: same method, denote 1 if `A[i + 1] > A[i]`, -1 if `A[i + 1] < A[i]`, 0 if `A[i + 1] == A[i]`. Then the number of non zero number should be equal to the sum of all number.

- Public solution

Use `increase` and `decrease`, set `increase = False` if there is `A[i + 1] > A[i]`, set `decrease = False` if there is `A[i] < A[i + 1]`. Then finally at least one of `increase` and `decrease` is True.

#### 905. Sort Array By Parity (array)

- My solution

Use two array to store even and odd numbers, then concatenate them together and output. This will use too much space.

- Public solution 

In-place: similar with the idea of quick sort, use two pointers `i` and `j` start from left and end, ideally the number at left of `i` are all even, and number at right of `j` are all odd; if `A[i]` is even, increase it, if `A[j]` is odd, decrease it; if `A[i]` is odd and `A[j]` is even, swap them. Terminate iteration when `i` meet with `j`.


#### 917. Reverse Only Letters (two pointers, stack)

- My solution

Two pointers: swap two letters pointed by two pointers `i`, `j` start from left and right, skip non-letters characters.

- Public solution

Stack: put all letters in a stack, then iterate through the string, if get a letter, then `pop()` the stack and append it to output; else, just append the character to output.

#### X. Tips and Notice

- Initialize iterate variable if use `while` loop.
- Always check the terminal condition of `while` loop.
- Be careful when index the last element, `x[length(x)]` will be out of index.
- Be careful for pop stack, need to check whether stack is empty.
- Be careful for empty input, especially for array
- Don't forget empty input case, in this case some methods cannot be invoked.
- Add `self.` before methods in class when use recursion in Python.
- For linked list, must check itself or next is None or not.
- Be careful for the condition in `while` loop.
- Difference of the cumulative sum (of array) is the number itself. 
- Be careful about variables defined in the loop, it is possible that the loop will not be executed, therefore will cause variable undefined error.
- Be careful when assigning python list to another object, need to use copy of the list rather than list itself.


