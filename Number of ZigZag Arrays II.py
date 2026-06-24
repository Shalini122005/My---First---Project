class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        size = 2 * m

        T = [[0] * size for _ in range(size)]

        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1
            for u in range(v + 1, m):
                T[m + v][u] = 1

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(n):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            n = len(M)
            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        vec = [0] * size

        for v in range(m):
            vec[v] = v
            vec[m + v] = m - 1 - v

        if n == 2:
            return sum(vec) % MOD

        P = mat_pow(T, n - 2)

        ans = 0
        for i in range(size):
            cur = 0
            for j in range(size):
                cur = (cur + P[i][j] * vec[j]) % MOD
            ans = (ans + cur) % MOD

        return ans
