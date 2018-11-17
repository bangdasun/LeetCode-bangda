class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        """
        ans = {('a', 'e', 'r'): ['are', 'ear', 'era'],
               ('a', 'b', 't'): ['bat', 'tab'],
               ('e', 'c', 'd', 'o'): ['code']}
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()