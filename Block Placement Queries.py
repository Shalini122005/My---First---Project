from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, idx, val, node, l, r):
        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)

        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, ql, qr, node, l, r):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2
        return max(
            self.query(ql, qr, node * 2, l, mid),
            self.query(ql, qr, node * 2 + 1, mid + 1, r)
        )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = 0
        for q in queries:
            mx = max(mx, q[1])

        obstacles = SortedList([0, mx])

        seg = SegmentTree(mx + 1)
        seg.update(mx, mx, 1, 0, mx)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                i = obstacles.bisect_left(x)
                left = obstacles[i - 1]
                right = obstacles[i]

                seg.update(right, right - x, 1, 0, mx)
                seg.update(x, x - left, 1, 0, mx)

                obstacles.add(x)

            else:
                x, sz = q[1], q[2]

                i = obstacles.bisect_right(x)
                left = obstacles[i - 1]

                best = seg.query(0, left, 1, 0, mx)
                best = max(best, x - left)

                ans.append(best >= sz)

        return ans
        
