# sort + two pointers
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1, n2 = len(nums1), len(nums2)
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        output = []
        
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
                
        return output
		
# hash table
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1, n2 = len(nums1), len(nums2)
        output = []
        
        nums1_table = {}
        for i in range(n1):
            if nums1[i] not in nums1_table.keys():
                nums1_table[nums1[i]] = 1
            else:
                nums1_table[nums1[i]] += 1
        
        for i in range(n2):
            if nums2[i] in nums1_table.keys():
                if nums1_table[nums2[i]] > 0:
                    nums1_table[nums2[i]] -= 1
                    output.append(nums2[i])
                
        return output