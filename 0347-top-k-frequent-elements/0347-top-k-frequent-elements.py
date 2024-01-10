class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        s = sorted(d.items(), key=lambda x : x[1])
        s.reverse()
        for i in range(k):
            l.append(s[i][0])
        return l