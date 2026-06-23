class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  # max heap (store negatives)
        large = []  # min heap
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed[num]:
                    delayed[num] -= 1
                    heappop(heap)
                else:
                    break

        def balance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                heappush(large, -heappop(small))
                small_size -= 1
                large_size += 1
                prune(small)

            elif small_size < large_size:
                heappush(small, -heappop(large))
                small_size += 1
                large_size -= 1
                prune(large)

        def add_num(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heappush(small, -num)
                small_size += 1
            else:
                heappush(large, num)
                large_size += 1

            balance()

        def remove_num(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large)

            balance()

        def get_median():
            if k & 1:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        for i in range(k):
            add_num(nums[i])

        ans = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            ans.append(get_median())

        return ans
