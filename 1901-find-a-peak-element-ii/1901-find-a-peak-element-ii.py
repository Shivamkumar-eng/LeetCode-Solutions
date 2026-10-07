class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        start_col, end_col = 0, n - 1

        while start_col <= end_col:
            mid_col = (start_col + end_col) // 2

            # Find row index of maximum element in current mid_col
            max_row = 0
            for r in range(1, m):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r

            # Check horizontal neighbors
            left_val = mat[max_row][mid_col - 1] if mid_col - 1 >= 0 else -1
            right_val = mat[max_row][mid_col + 1] if mid_col + 1 < n else -1

            current_val = mat[max_row][mid_col]

            # If current element is greater than both left and right, it's a peak
            if current_val > left_val and current_val > right_val:
                return [max_row, mid_col]
            # Move towards the larger neighbor
            elif left_val > current_val:
                end_col = mid_col - 1
            else:
                start_col = mid_col + 1

        return []