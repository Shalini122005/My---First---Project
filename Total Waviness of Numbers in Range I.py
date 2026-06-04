from functools import lru_cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n):
            if n < 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dp(pos, tight, started, length, prev2, prev1):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, 0, -1, -1)
                        total_count += cnt
                        total_waviness += wav
                    else:
                        if not started:
                            cnt, wav = dp(pos + 1, ntight, True, 1, -1, d)
                            total_count += cnt
                            total_waviness += wav
                        else:
                            add = 0

                            if length >= 2:
                                if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                    add = 1

                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                min(length + 1, 3),
                                prev1,
                                d
                            )

                            total_count += cnt
                            total_waviness += wav + add * cnt

                return (total_count, total_waviness)

            return dp(0, True, False, 0, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)
