class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        num=0
        strr=""
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='[':
                st.append((strr,num))
                num=0
                strr=""
            elif ch==']':
                prev,num1=st.pop()
                strr=prev+num1*strr
            else:
                strr+=ch
        return strr
