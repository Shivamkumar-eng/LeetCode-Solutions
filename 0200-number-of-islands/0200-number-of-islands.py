class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Counts the number of distinct islands in a 2D binary grid.
        '1' represents land, '0' represents water.
        """
        # 1. Base check: Return 0 if grid is empty
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        # 2. Recursive helper to visit and sink connected land
        def dfs(r: int, c: int) -> None:
            # Stop if out of grid bounds OR if cell is water ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # Sink current land cell by marking it as water ('0')
            grid[r][c] = '0'

            # Traverse all 4 cardinal directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # 3. Scan every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1  # Discovered a new island
                    dfs(r, c)     # Sink the entire island and all attached land

        return islands


# Example Usage:
if __name__ == "__main__":
    solution = Solution()

    example_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    result = solution.numIslands(example_grid)
    print(f"Number of islands: {result}")  # Output: 3