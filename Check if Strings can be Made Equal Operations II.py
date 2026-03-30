class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = Counter()
        odd1 = Counter()
        even2 = Counter()
        odd2 = Counter()
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even1[s1[i]] += 1
                even2[s2[i]] += 1
            else:
                odd1[s1[i]] += 1
                odd2[s2[i]] += 1
        
        return even1 == even2 and odd1 == odd2
