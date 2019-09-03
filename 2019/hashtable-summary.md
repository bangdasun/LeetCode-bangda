
## Summary



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
- Sliding window algorithm template for substring problems: [template](https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.) by [ChaoyangHe](https://leetcode.com/chaoyanghe/).
- Usage of built-in packages of Python like `collections`, `itertools`.
- Don't use `[[0] * c] * r` to create 2D Python array, `*` will create copy. Use list comprehension instead: `[[0 for i in range(c)] for j in range(r)]`.
