class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        tab=[]
        for i in range(len(s)):
            if (i//k)%2==0:
               tab.insert(i-i%k,s[i])
            else:
                tab.append(s[i])
        res=""
        for t in tab:
            res+=t
        return res
