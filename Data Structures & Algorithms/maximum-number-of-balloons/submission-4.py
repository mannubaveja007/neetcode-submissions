class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = Counter(text)
        targetmap = Counter("balloon")

        res = len(text)
        for c in targetmap:
            res = min(res,hashmap[c] // targetmap[c])
        return res