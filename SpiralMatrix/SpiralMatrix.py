class Solution:
    def spiralOrder(self, matrix):
        curr_dir = 'right'
        curr_row = 0
        curr_col = 0
        res = [matrix[curr_row][curr_col]]
        matrix[curr_row][curr_col] = -999

        while len(res) != len(matrix[0]) * len(matrix):
            # Go right
            if curr_dir ==  'right':
                curr_col += 1
                if curr_col >= len(matrix[0]) or matrix[curr_row][curr_col] == -999:
                    curr_col -= 1
                    curr_dir = 'down'
                else:
                    res.append(matrix[curr_row][curr_col])
                    matrix[curr_row][curr_col] = -999
            # Go down
            elif curr_dir == 'down':
                curr_row += 1
                if curr_row >= len(matrix) or matrix[curr_row][curr_col] == -999:
                    curr_row -= 1
                    curr_dir = 'left'
                else:
                    res.append(matrix[curr_row][curr_col])
                    matrix[curr_row][curr_col] = -999
            # Go left
            elif curr_dir ==  'left':
                curr_col -= 1
                if curr_col < 0 or matrix[curr_row][curr_col] == -999:
                    curr_col += 1
                    curr_dir = 'up'
                else:
                    res.append(matrix[curr_row][curr_col])
                    matrix[curr_row][curr_col] = -999
            # Go up
            elif curr_dir == 'up':
                curr_row -= 1
                if curr_row < 0 or matrix[curr_row][curr_col] == -999:
                    curr_row += 1
                    curr_dir = 'right'
                else:
                    res.append(matrix[curr_row][curr_col])
                    matrix[curr_row][curr_col] = -999
                    
        return res

solution = Solution()
ans = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]); assert ans == [1,2,3,6,9,8,7,4,5], ans
ans = solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]); assert ans == [1,2,3,4,8,12,11,10,9,5,6,7], ans
