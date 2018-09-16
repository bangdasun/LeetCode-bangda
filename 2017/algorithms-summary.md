
## Summary

### Math

#### [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/solution/)

Algorithm: Time `O(nlogn)`, space `O(1)`

Revert the "half" part of the number, compare the first half and second half of the number, which requires get the digits from back to front (and remove it simultaneously).

* Use **modulus** (by 10) to get digits of number one by one from back to front.
* Number of digits is odd: 
```
12321 % 10 = 1; 12321 / 10 = 1232; 1 = 1
1232 % 10 = 2; 1232 / 10 = 123; 1 * 10 + 2 = 12
123 % 10 = 3; 123 / 10 = 12; 12 * 10 + 3 = 123
```
* Number of digits is even
```
1221 % 10 = 1; 1221 / 10 = 122; 1 = 1
122 % 10 = 2; 122 / 10 = 12; 1 * 10 + 2 = 12
```

Alternatives:

* Convert number into string: this requires extra space `O(n)`. While in python this method could be done in one line `str(x) == str(x)[::-1]`.

Corner case:

* Negative integers are not palindrome since `-` is not equal to the last digit.

Solutions: [Java](https://github.com/bangdasun/LeetCode-bangda/blob/master/Algorithms/easy-PalindromeNumber.java), [Python](https://github.com/bangdasun/LeetCode-bangda/blob/master/Algorithms/easy-PalindromeNumber.py)


#### [202. Happy Number](https://leetcode.com/problems/happy-number/description/)

Happy number: continue doing sum square of all digits of a number and can get 1:
```
19:
1 * 1 + 9 * 9 = 82
8 * 8 + 2 * 2 = 68
6 * 6 + 8 * 8 = 100
1 * 1 + 0 * 0 + 0 * 0 = 1
```
If the number is not a happy number there would be a circle in this process.

Algorithm: Time `O(?)`, space `O(1)` 

We can detect whether there is a "circle" during the process (Floyd Cycle detection algorithm). This algorithm is also used in detecting cycle in linked list.

* Use two pointers (slow and fast), where `sumSquare()` will be applied on fast pointer twice: keep running while `fast != slow` and when `fast == 1` means this is a happy number; when `fast == slow` and they are not 1, means there is a cycle. 
* Calculate the sum square based on using modulus to get digits of a number.

Alternatives:

* (My AC solution): store all sum square in a HashMap and check return `false` if the new value is already contained in HashMap. Time `O(?)`, space `O(n)`.


Corner case:


Solutions: [Java](https://github.com/bangdasun/LeetCode-bangda/blob/master/Algorithms/easy-HappyNumber.java), [Two Pointers](https://discuss.leetcode.com/topic/12587/my-solution-in-c-o-1-space-and-no-magic-math-property-involved)


#### [202. Power of Two](https://leetcode.com/problems/power-of-two/description/)

Algorithm: Time `O(1)`, space `O(1)`

Bit operation (to be continued...)

Alternatives:

* (My AC solution): Recursion. When `n>1` and `n` is even, check `n/2`, base case: `n = 1`. Time `O(logn)`, space `O(1)`.
* Iterative: Time and space complexity same as recursion.

Corner case:

Solutions: [Java](https://github.com/bangdasun/LeetCode-bangda/blob/master/Algorithms/easy-PowerOfTwo.java), [Bit Operation](https://leetcode.com/problems/power-of-two/discuss/)


#### [258. Add Digits](https://leetcode.com/problems/add-digits/description/)

Algorithm: Time `O(1)`, space `O(1)`

**Math property**: take a three digits number `x` as an example, `x = 100 * a + 10 * b + c`, use **modulus** by 9: `(100 * a + 10 * b + c) % 9 = (a + b+ c) % 9`.

* If `x` is less than 9 or it's greater than 9 but not a 9 multiple, `x % 9 = x`; if `x` is a multiple of 9, `x % 9 = 0`, and we need to return 9.

Alternatives:

Corner case:

Solutions: [Java](https://github.com/bangdasun/LeetCode-bangda/blob/master/Algorithms/easy-AddDigits.java)


#### [268. Missing Number](https://leetcode.com/problems/missing-number/description/)

Algorithm:

XOR (to be continued...)

Alternatives:

* (My AC solution): try to append all digits into a HashMap, then check the values in HashMap one by one: if HashMap doesn't contain `x+1`, and `x` is less than `n` (ideally the array is `[0, 1, 2, ... , n]`), then `x+1` is missing; if HashMap doesn't contain `x-1` and `x` is greater then 0, then `x-1` is missing. Time `O(n)`, space `O(n)`.
* Binary search: use `Arrays.sort(nums)` first. (to be continued...)

Corner case:

Solutions: [Java](https://github.com/bangdasun/LeetCode-bangda/blob/master/Algorithms/easy-MissingNumber.java)

