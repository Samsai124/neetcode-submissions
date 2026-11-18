class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        maps = set()
        for i in range(0,9):
            maps = set()
            for val in board[i]:
                if(val in maps):
                    return False
                if val != '.':
                    maps.add(val)
            
        for col in zip(*board):
            maps = set()
            for val in col:
                if(val in maps):
                    return False
                if val != '.':
                    maps.add(val)
        for i in range(0,9,3):
            for j in range(0,9,3):
                maps = set()
                for k in range(0,3):
                    for l in range(0,3):
                        if board[i+k][j+l] in maps:
                            return False
                        if board[i+k][j+l] != '.':
                            maps.add(board[i+k][j+l])

        return True
        