from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        x = y = 0
        d = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        ans = 0
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(c):
                    if (x + dx, y + dy) in obs:
                        break
                    x += dx
                    y += dy
                    ans = max(ans, x*x + y*y)
        
        return ans
