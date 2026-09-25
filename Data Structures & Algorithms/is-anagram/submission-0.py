class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counts = {}
        countt = {}

        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for x in t:
            countt[x] = countt.get(x, 0) + 1
        if counts == countt:
            return True
        else:
            return False
