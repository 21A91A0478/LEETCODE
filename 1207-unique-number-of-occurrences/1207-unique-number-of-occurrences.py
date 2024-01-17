class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        v = d.values()
        return len(v)==len(set(v))