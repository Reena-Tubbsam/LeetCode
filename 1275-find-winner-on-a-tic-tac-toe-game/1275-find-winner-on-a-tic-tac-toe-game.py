class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [] # [["","",""],["","",""],["","",""]]
        for i in range(3):
            grid.append([""] * 3)
        for i, (row, col) in enumerate(moves):
            player = ""
            if i % 2 == 0 :
                player = "A"
            else:
                player = "B"
            grid[row][col] = player
            if grid[row][0] == grid[row][1] == grid[row][2] == player:
                return player
            elif grid[0][col] == grid[1][col] == grid[2][col] == player:
                return player
            elif (row == col) and grid[0][0] == grid[1][1] == grid[2][2] == player:
                return player
            elif (row + col == 2) and grid[0][2] == grid[1][1] == grid[2][0] == player:
                return player
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
        
        