class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                res.append(arr[i])
        
        if len(res) >= k:
            return res[k-1]
        else:
            return ""