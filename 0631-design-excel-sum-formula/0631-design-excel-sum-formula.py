class Excel:

    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord('A') + 1
        self.matrix = [[0] * self.width for _ in range(self.height)]
        self.formulas = {}

    def set(self, row: int, column: str, val: int) -> None:
        col_index = ord(column) - ord('A')
        self.matrix[row - 1][col_index] = val
        if (row, column) in self.formulas:
            del self.formulas[(row, column)]

    def get(self, row: int, column: str) -> int:
        col_index = ord(column) - ord('A')
        if (row, column) in self.formulas:
            return self._calculate_sum(row, column)
        return self.matrix[row - 1][col_index]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.formulas[(row, column)] = numbers
        return self._calculate_sum(row, column)

    def _calculate_sum(self, row: int, column: str) -> int:
        total = 0
        for formula in self.formulas[(row, column)]:
            if ':' in formula:
                start, end = formula.split(':')
                start_col, start_row = start[0], int(start[1:])
                end_col, end_row = end[0], int(end[1:])
                for r in range(start_row, end_row + 1):
                    for c in range(ord(start_col) - ord('A'), ord(end_col) - ord('A') + 1):
                        total += self.get(r, chr(c + ord('A')))
            else:
                col, r = formula[0], int(formula[1:])
                total += self.get(r, col)
        return total
