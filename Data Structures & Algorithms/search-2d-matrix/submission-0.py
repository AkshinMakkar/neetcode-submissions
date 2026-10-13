class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)       # Number of rows
        n = len(matrix[0])    # Number of columns

        t = m * n            # Total numbers
        l = 0                # Left pointer
        r = t - 1            # Right pointer

        while l <= r:
            mid = (l + r) // 2  # Find middle index

            i = mid // n        # Find row
            j = mid % n         # Find column

            mid_num = matrix[i][j]  # Get middle number

            if target == mid_num:
                return True

            elif target < mid_num:
                r = mid - 1     # Search left half

            else:
                l = mid + 1     # Search right half

        return False