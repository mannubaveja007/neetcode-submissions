class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        idx = []
        expected  = sorted(heights)
        for i in range(len(heights)):
            if (heights[i] != expected[i]):
                idx.append(i)

        return len(idx)
        