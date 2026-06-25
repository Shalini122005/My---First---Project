class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, t):
            drop = len(nums) - t
            stack = []
            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:t]

        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res

        ans = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            part1 = pick(nums1, i)
            part2 = pick(nums2, k - i)

            cand = merge(part1[:], part2[:])

            if cand > ans:
                ans = cand

        return ans
