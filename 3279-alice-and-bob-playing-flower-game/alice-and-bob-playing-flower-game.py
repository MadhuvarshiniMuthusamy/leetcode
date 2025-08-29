class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odds_x=(n+1)//2
        even_x=n//2
        odds_y=(m+1)//2
        even_y=m//2
        return (odds_x*even_y)+(odds_y*even_x)