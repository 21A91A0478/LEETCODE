class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d1 = {}
        d2 = {}
        for i,j in matches:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
            
            if j not in d2:
                d2[j] = 1
            else:
                d2[j] += 1
        
        l1 = []
        l2 = []
        for i in d1.keys():
            if i not in d2:
                l1.append(i)
            
        for i, j in d2.items():
            if j==1:
                l2.append(i)
            
        l1.sort()
        l2.sort()
        return [l1, l2]
    
        