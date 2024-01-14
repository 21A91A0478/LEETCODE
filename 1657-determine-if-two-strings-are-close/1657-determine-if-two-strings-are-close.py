class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in word1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for j in word2:
            if j not in d2:
                d2[j] = 1
            else:
                d2[j] += 1
        
        return sorted(d1.values())==sorted(d2.values()) and sorted(d1.keys())==sorted(d2.keys())