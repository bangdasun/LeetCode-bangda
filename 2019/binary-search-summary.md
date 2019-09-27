
## Binary Search Summary

### 1. Binary Search Time Complexity

From `T(n) = T(n/2) + O(1)` we can get`O(logn)`. Therefore if it requires to solve the problem in `O(logn)` or have a better solution than `O(n)`, it is highly possible to use binary search.

### 2. Binary Search General Template

There are 4 key components for the template:

1. start + 1 < end
2. mid = (start + end) // 2
3. A[mid] ==, <, >
4. A[start], A[end] ? target

The key idea for binary search is **reduce solution space**, rather than find the solution directly.

#### 2.1 Example #35 - Search Insert Position

```python
class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0
        
        start, end = 0, n - 1
        # 1. start + 1 < end
        while start + 1 < end:
            # 2. mid = (start + end) // 2
            mid = (start + end) // 2
            # 3. A[mid] ==, <, >
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
        # 4. A[start], A[end] ? target
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        if nums[end] < target:
            return end + 1
```

Other examples:

- #69 - Sqrt(x)
- #74 - Search a 2D Matrix

- #167 - Two Sum II - Input Array is Sorted
- #240 - Search a 2D Matrix II
- #367 - Valid Perfect Square

### 3. Find the First or Last Position of XXX

Find the first or last position of some specific differences. Things to notice is that in last step, **we need to first check the start position if we're looking for "first" position, then check the last position**; vice versa.

#### 3.1 Example #34 - Find First and Last Position of Element in Sorted Array

```python
class Solution:
    def searchFirst(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
        
        # look for first first
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
        
    def searchLast(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid
        
        # look for last first
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_loc = self.searchFirst(nums, target)
        last_loc = self.searchLast(nums, target)
        return [first_loc, last_loc]
```

Other examples:

- #153 - Find Minimum in Rotated Sorted Array (first position less than or equal to last number, since the array can be not rotated, then first number if less than last number)
- #154 - Find Minimum in Rotated Sorted Array II (follow up of #153, cannot be done in `O(logn)`)
- #278 - First Bad Version
- #744 - Find Smallest Letter Greater Than Target
- lintcode #458 - Last Position of Target

### 4. Half Half

Cannot be solved directly, keep the half with solution or drop the half without solution. Can be turn into other formats like first / last position of XXX.

#### 4.1 Example #33 - Search in Rotated Sorted Array

First find the start point of original, i.e. Find minimum in rotated sorted array. Then do binary search.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        start, end = 0, n - 1
        compare_num = nums[-1]
        
        # binary search to find original start
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > compare_num:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            min_index = start
        else:
            min_index = end
        
        # binary search on reduced array
        if target <= compare_num:
            new_start, new_end = min_index, n - 1
        else:
            new_start, new_end = 0, min_index
        
        while new_start + 1 < new_end:
            new_mid = (new_start + new_end) // 2
            if nums[new_mid] < target:
                new_start = new_mid
            else:
                new_end = new_mid
        
        if nums[new_start] == target:
            return new_start
        if nums[new_end] == target:
            return new_end
        
        return -1
```



Other examples

- #81 - Search in Rotated Sorted Array II (follow up, same as #154, cannot be solved in `O(logn)`)
- #162 - Find Peak Element (first position to decrease, either one is valid solution)
- #658 - Find K Closest Elements
- #852 - Peak Index in a Mountain Array (first position to decrease)

### 5. Other Types

#### 5.1 Example #428 - Pow(x, n)

```python
# recursive
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n/2) * x^(n/2)
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, -n)
        
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        
        if n % 2 == 1:
            return self.myPow(x * x, n // 2) * x
        
# iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n/2) * x^(n/2)
        
        # x^n = (x^(-1))^n
        if n < 0:
            x = 1 / x
            n = -n
            
        output = 1
        current_product = x
        
        while n > 0:
            if n % 2 == 1:
                output = output * current_product
            current_product = current_product * current_product
            n //= 2
        
        return output
```

#### 5.2 Example - lintcode #140 - Fast Power

```python
# recursive
class Solution:
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
            
        if n == 1:
            return a % b
            
        # a^n = (a^n/2) ^ 2
        power = self.fastPower(a, b, n // 2)
        power = (power * power) % b
        
        if n % 2 == 1:
            power = (power * a) % b
            
        return power

# iterative
class Solution:
    def fastPower(self, a, b, n):
        output = 1
        while n > 0:
            if n % 2 == 1:
                output = (output * a) % b
            a = a * a % b
            n = n // 2
        return output % b
```



#### X. Tips and Notice

