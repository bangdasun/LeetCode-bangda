class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0:
            return []
        
        output = []
        nums1_count = {}
        for num in nums1:
            if num not in nums1_count:
                nums1_count[num] = 1
            else:
                nums1_count[num] += 1
        
        for num in nums2:
            if num in nums1_count:
                output.append(num)
        
        return list(set(output))
