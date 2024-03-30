class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        max_col_heights = list()
        max_row_heights = list()
        for row_index, col_index in zip(range(len(min(grid))), range(len(grid))):
            max_row_heights.append(max(grid[col_index]))
            max_col_heights.append(max([grid[new_col_index][row_index] for new_col_index in range(len(grid))]))

        sum = 0
        for row_index in range(len(min(grid))):
            for col_index in range(len(grid)):
                sum+=min(max_col_heights[col_index], max_row_heights[row_index]) - grid[row_index][col_index]
        return sum

obj = Solution()
grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]
obj.maxIncreaseKeepingSkyline(grid)