class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # Directions: N, E, S, W
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx = 0  # start facing north
        
        x, y = 0, 0
        max_dist = 0
        
        # Convert obstacles to set for fast lookup
        obstacle_set = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd == -2:  # turn left
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:  # turn right
                dir_idx = (dir_idx + 1) % 4
            else:  # move forward cmd steps
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist
