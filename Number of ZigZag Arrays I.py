class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        
        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        if n == 2:
            return sum(up[1:]) + sum(down[1:]) % MOD

        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            for i in range(1, m + 1):
                pref_down[i] = (pref_down[i - 1] + down[i]) % MOD

            suff_up = [0] * (m + 2)
            for i in range(m, 0, -1):
                suff_up[i] = (suff_up[i + 1] + up[i]) % MOD

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            for x in range(1, m + 1):
                new_up[x] = pref_down[x - 1]
                new_down[x] = suff_up[x + 1]

            up = new_up
            down = new_down

        ans = 0
        for v in range(1, m + 1):
            ans = (ans + up[v] + down[v]) % MOD

        return ans
