class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        layer = 0
        while True:
            total_sum = (layer + 1 ) * layer / 2
            if total_sum > n:
                layer -= 1
                break
            layer += 1
            
        return layer
		
