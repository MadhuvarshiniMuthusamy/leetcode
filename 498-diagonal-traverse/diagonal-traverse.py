class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        result=[]
        for diag in range(rows+cols-1):
            diagele=[]
            row=0 if diag<cols else diag-cols+1
            col=diag if diag<cols else cols-1
            while row<rows and col>=0:
                diagele.append(mat[row][col])
                row+=1
                col-=1
            if diag%2==0:
                result.extend(reversed(diagele))
            else:
                result.extend(diagele)
        return result