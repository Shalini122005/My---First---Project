from typing import List
from bisect import bisect_left
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def build(start, duration):
            rides = sorted(zip(start, duration))

            s = [x for x, _ in rides]
            n = len(rides)

            suffix_min = [0] * n
            suffix_min[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suffix_min[i] = min(
                    suffix_min[i + 1],
                    rides[i][0] + rides[i][1]
                )

            prefix_min_dur = [0] * n
            prefix_min_dur[0] = rides[0][1]

            for i in range(1, n):
                prefix_min_dur[i] = min(
                    prefix_min_dur[i - 1],
                    rides[i][1]
                )

            return s, suffix_min, prefix_min_dur

        water_s, water_suffix, water_prefix_dur = build(
            waterStartTime, waterDuration
        )

        land_s, land_suffix, land_prefix_dur = build(
            landStartTime, landDuration
        )

        INF = float('inf')
        ans = INF

       
        for ls, ld in zip(landStartTime, landDuration):
            x = ls + ld
            idx = bisect_left(water_s, x)

            best = INF

            if idx < len(water_s):
                best = min(best, water_suffix[idx])

            if idx > 0:
                best = min(best, x + water_prefix_dur[idx - 1])

            ans = min(ans, best)

        
        for ws, wd in zip(waterStartTime, waterDuration):
            y = ws + wd
            idx = bisect_left(land_s, y)

            best = INF

            if idx < len(land_s):
                best = min(best, land_suffix[idx])

            if idx > 0:
                best = min(best, y + land_prefix_dur[idx - 1])

            ans = min(ans, best)

        return ans
