class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        output = []
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 < 1 or n2 < 1:
            return []
        
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1_sorted[i] < nums2_sorted[j]:
                i += 1
            elif nums1_sorted[i] > nums2_sorted[j]:
                j += 1
            else:
                output.append(nums1_sorted[i])
                i += 1
                j += 1
        
        output = list(set(output))
        return output