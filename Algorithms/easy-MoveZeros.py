# https://leetcode.com/problems/move-zeroes/description/
# optimal - https://leetcode.com/problems/move-zeroes/solution/

def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)

moveZeros([0, 1, 0, 3, 12])
