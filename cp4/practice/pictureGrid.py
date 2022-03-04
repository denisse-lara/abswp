
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# reverses the grid, making cols to rows
newGrid = [[grid[x][y] for x in range(len(grid))] for y in range(len(grid[0]))]
# joins all the characters in each row and then separates each row with a newline
print(*list(map(lambda x: ''.join(x), newGrid)), sep='\n')
