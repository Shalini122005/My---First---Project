from typing import List
from bisect import bisect_left
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        INF = float('inf')

        
        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [a for a, b in rides]
            d = [b for a, b in rides]
            n = len(rides)

            prefix_min_d = [INF] * n
            prefix_min_d[0] = d[0]
            for i in range(1, n):
                prefix_min_d[i] = min(prefix_min_d[i - 1], d[i])

            suffix_min_sd = [INF] * n
            suffix_min_sd[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suffix_min_sd[i] = min(suffix_min_sd[i + 1], s[i] + d[i])

            def query(x):
                k = bisect_left(s, x)
                ans = INF

                if k > 0:
                    ans = min(ans, x + prefix_min_d[k - 1])

                if k < n:
                    ans = min(ans, suffix_min_sd[k])

                return ans

            return query

        water_query = build(waterStartTime, waterDuration)
        land_query = build(landStartTime, landDuration)

        ans = INF

        
        for ls, ld in zip(landStartTime, landDuration):
            ans = min(ans, water_query(ls + ld))

        
        for ws, wd in zip(waterStartTime, waterDuration):
            ans = min(ans, land_query(ws + wd))

        return ans
