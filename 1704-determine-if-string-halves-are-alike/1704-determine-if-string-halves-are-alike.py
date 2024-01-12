class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def fun(s):
            c = 0
            st = "aeiouAEIOU"
            for i in s:
                if i in st:
                    c += 1
            return c
        
        
        n = len(s)//2
        s1 = s[:n]
        s2 = s[n:]
        return fun(s1)==fun(s2)
        