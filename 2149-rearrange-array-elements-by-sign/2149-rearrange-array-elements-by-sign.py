class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = [i for i in nums if i > 0]
        n = [i for i in nums if i < 0]
        l = []
        for i in range(len(p)):
            l.append(p[i])
            l.append(n[i])
        return l