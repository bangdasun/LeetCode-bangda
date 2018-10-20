class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        n_bed = len(flowerbed)
        if n_bed == 1:
            if flowerbed == [0]:
                return n <= 1
            else:
                return n == 0
                
        left, right = [n_bed] * n_bed, [n_bed] * n_bed
        
        
        for i in range(n_bed):
            if flowerbed[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1
        
        for i in range(n_bed - 1, -1, -1):
            if flowerbed[i] == 1:
                right[i] = 0
            elif i < n_bed - 1:
                right[i] = right[i + 1] + 1
        
        cnt = 0
        cnt_list = []
        dist = []
        for i in range(n_bed):
            dist.append(min(left[i], right[i]))
            
            if dist[i] > 1:
                cnt += 1
                
            if dist[i] <= 1 and cnt > 0:
                cnt_list.append(cnt)
                cnt = 0
        
        if cnt > 0:
            cnt_list.append(cnt)
                
        num_available = 0
        for i in cnt_list:
            num_available += i // 2 + i % 2
        
        return num_available >= n
			
# simple and more direct solution
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        bed_len = len(flowerbed)
        cnt = 0
        i = 0
        while i < bed_len:
		    # the logic is a little tricky
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == bed_len - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                cnt += 1
            i += 1
        
        return cnt >= n