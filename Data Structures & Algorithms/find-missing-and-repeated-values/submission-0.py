class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hashmap = defaultdict(int)
        for i in range(n):
            for j in range(n):
                hashmap[grid[i][j]]+=1
        double , missing = 0,0
        for num in range(1,n*n+1):
            if hashmap[num] >1:
                double = num
            
            if hashmap[num] == 0 :
                missing = num

        return [double,missing]