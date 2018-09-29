# move count should be symmetric
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_cnt = [0, 0, 0, 0]
        for m in moves:
            if m == 'L':
                moves_cnt[0] += 1
            elif m == 'R':
                moves_cnt[1] += 1
            elif m == 'U':
                moves_cnt[2] += 1
            elif m == 'D':
                moves_cnt[3] += 1
        return len(set(moves_cnt[:2])) == 1 and len(set(moves_cnt[2:])) == 1
		
		
# coordinates
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # coordinates in 2D plane
        x, y = 0, 0
        for m in moves:
            if m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
            elif m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
                
        return x == 0 and y == 0