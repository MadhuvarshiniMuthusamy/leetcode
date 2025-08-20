class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1]]
        for i in range(1,numRows):
            row=[1]
            prev=triangle[-1]
            for j in range(1,len(prev)):
                row.append(prev[j-1]+prev[j])
            row.append(1)
            triangle.append(row)
        return triangle