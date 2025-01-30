class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidUnit(unit):
            seen = set()
            for num in unit:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        # Check rows
        for row in board:
            if not isValidUnit(row):
                return False

        # Check columns
        for col in zip(*board):
            if not isValidUnit(col):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not isValidUnit(sub_box):
                    return False

        return True
