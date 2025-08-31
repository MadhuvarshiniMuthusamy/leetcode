class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                if num in rows[i]:
                    return False
                rows[i].add(num)
                if num in cols[j]:
                    return False
                cols[j].add(num)
                bi=(i//3)*3+(j//3)
                if num in boxes[bi]:
                    return False
                boxes[bi].add(num)
        return True