class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        count=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                x1,y1=points[i]
                x2,y2=points[j]
                if x1<=x2 and y2<=y1:
                    valid=True
                    for k in range(n):
                        if i==k or j==k:
                            continue
                        x,y=points[k]
                        if x1<=x<=x2 and y2<=y<=y1:
                            valid=False
                            break
                    if valid:
                        count+=1
        return count