class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        # Track horizontal and vertical displacement
        x, y = 0, 0
        
        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
        
        # Robot returns to origin if both x and y are zero
        return x == 0 and y == 0
