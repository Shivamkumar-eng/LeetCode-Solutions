class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
         return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
        # 1. Move Right across the top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

        # 2. Move Down along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

        # 3. Move Left across the bottom row (if row remains)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

        # 4. Move Up along the left column (if column remains)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result