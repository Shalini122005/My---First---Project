class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        for bill in bills:
            if bill==5:
                f+=1
            elif bill==10:
                t+=1
                if f==0:
                    return False
                f-=1
            else:
                if t>0 and f>0:
                    t-=1
                    f-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True
