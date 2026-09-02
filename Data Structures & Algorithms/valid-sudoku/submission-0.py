class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subBox = [[set()for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == ".":
                    continue
                if current in rows[r] or current in cols[c] or current in subBox[r//3][c//3]:
                    return False
                rows[r].add(current)
                cols[c].add(current)
                subBox[r//3][c//3].add(current)  
        return True
        