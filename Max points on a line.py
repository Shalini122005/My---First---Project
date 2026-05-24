from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        result = 1

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)

                dx //= g
                dy //= g
                if dx < 0:
                    dx *= -1
                    dy *= -1

                if dx == 0:
                    dy = 1

                if dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1

                result = max(result, slopes[(dx, dy)] + 1)

        return result
