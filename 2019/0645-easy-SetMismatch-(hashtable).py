class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_count = {}
        output = []
        
        for num in nums:
            if num in nums_count:
                output.append(num)
                break
            else:
                nums_count[num] = 1
        
        total_sum = (1 + n) * n // 2
        partial_sum = sum(nums) - output[0]
        output.append(total_sum - partial_sum)
        return output
