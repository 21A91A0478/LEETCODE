class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 = {}
        d2 = {}
        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        
        for j in t:
            if j not in d2:
                d2[j] = 1
            else:
                d2[j] += 1
        
        c = 0
        for i, j in d1.items():
            if i not in d2:
                c += j
            elif d1[i] > d2[i]:
                c += (d1[i]-d2[i])
        return c
        
        