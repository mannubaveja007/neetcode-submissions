class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        idx = 0
        res = []
        for i in range(1,n+1):
            while(idx < n and nums[idx] < i):
                idx+=1
            if (idx==n or nums[idx] > i):
                res.append(i)
        return res