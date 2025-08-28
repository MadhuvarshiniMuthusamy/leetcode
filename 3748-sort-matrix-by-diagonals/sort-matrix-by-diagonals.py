class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        diag={}
        for i in range(n):
            for j in range(n):
                key=i-j
                if key not in diag:
                    diag[key]=[]
                diag[key].append(grid[i][j])
        for key in diag:
            if key>=0:
                diag[key].sort(reverse=True)
            else:
                diag[key].sort()
        idx={key: 0 for key in diag}
        for i in range(n):
            for j in range(n):
                key=i-j
                grid[i][j]=diag[key][idx[key]]
                idx[key]+=1
        return grid
        