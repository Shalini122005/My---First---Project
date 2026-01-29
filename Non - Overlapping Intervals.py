class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ends=[]
        for s,e in intervals:
            ends.append((e,s))
        ends.sort()
        count=0
        last_end=ends[0][0]
        for e,s in ends[1:]:
            if s<last_end:
                count+=1
            else:
                last_end=e
        return count
