class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if numRows == 1:
            return s

        row = 0
        direction = 1

        rows = []

        for j in range(numRows):
            rows.append("")

        for ch in s:
            rows[row] = rows[row] + ch

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row = row + direction

        ans = ""

        for i in rows:
            ans = ans + i

        return ans