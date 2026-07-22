class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows: 
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s: 
                    return False 
                elif item != '.':
                    s.add(item)

        # columns: 
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s: 
                    return False 
                elif item != '.':
                    s.add(item)

        # valid boxes: 
        # starting points:
        starts = [(0,0), (0,3), (0,6), 
                  (3,0), (3, 3), (3, 6), 
                  (6, 0), (6, 3), (6, 6)
        ]
        # go through (i,j) in each of the starting points 
        for i, j in starts: 
            s = set() # make an empty set to store each digit we pass through 
            for row in range(i, i+3): # here we increment by 3 to get to the end point for each 3 x 3 box we have 
                for column in range(j, j+3):
                    item = board[row][column]
                    if item in s: 
                        return False # return false because the value reappears 
                    elif item != '.': # we don't want to count a empty place in the set 
                        s.add(item)

        return True 

        # time complexity of O(1) since we used a hash map for item storage 
        # space = O(1)
