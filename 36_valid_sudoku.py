# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9

        # Use sets to record the status of rows, columns, and boxes
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]

                # Skip empty cells
                if val == '.':
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the 3x3 box
                idx = (r // 3) * 3 + (c // 3)  # Calculate the box index
                #   Formula for nxn boxes
                #  sub_box_size = int(4 ** 0.5)  # 2
                # idx = (r // 2) * 2 + (c // 2)
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
