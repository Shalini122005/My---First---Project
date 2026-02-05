class Solution:
    def generate(self, ind, curr, ans, candidates, target):
        if target == 0:
            ans.append(curr.copy())
            return
        if target < 0:
            return
        
        for i in range(ind, len(candidates)):
            # Skip duplicates
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            # If current candidate is greater than target, break (because array is sorted)
            if candidates[i] > target:
                break
            curr.append(candidates[i])
            self.generate(i + 1, curr, ans, candidates, target - candidates[i])
            curr.pop()
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.generate(0, [], ans, candidates, target)
        return ans
