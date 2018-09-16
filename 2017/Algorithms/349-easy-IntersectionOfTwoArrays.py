# https://leetcode.com/problems/intersection-of-two-arrays/description/

def intersection(nums1, nums2):
    lookup = {}
    len_short, len_long = 0, 0
    ans = []
    
    if len(nums1) <= len(nums2):
        len_short = len(nums1)
        len_long = len(nums2)
    else:
        len_short = len(nums2)
        len_long = len(nums1)
    
    for i in range(len_long):
        if len(nums1) < len(nums2):
            lookup[str(nums2[i])] = i
        else:
            lookup[str(nums1[i])] = i
    
    for i in range(len_short):
        if len(nums1) < len(nums2):
            if lookup.has_key(str(nums1[i])):
                ans.append(nums1[i])
        else:
            if lookup.has_key(str(nums2[i])):
                ans.append(nums2[i])
    
    return list(set(ans))

nums1 = []
nums2 = [2, 2, 0]
intersection(nums1, nums2)
