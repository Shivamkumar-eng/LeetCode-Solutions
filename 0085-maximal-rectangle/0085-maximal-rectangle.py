class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        def largestRectangleArea(heights):
            stack = []
            mx = 0
            heights.append(0)
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    mid_height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    mx = max(mx, mid_height * width)
                stack.append(i)
            heights.pop()
            return mx

        c = len(matrix[0])
        heights = [0] * c
        mxa = 0
        
        for row in matrix:
            for j in range(c):
                # Update histogram height for the current row profile
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            mxa = max(mxa, largestRectangleArea(heights))
            
        return mxa
