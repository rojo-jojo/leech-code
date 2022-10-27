class Percolation:
    # create n by n grid, with all sides initially blocked
    def __init__(self, n: int):
        self.n = n
        self.grid = [[0]*(n) for x in range(n)]

    def showgrid(self) -> None:
        for x in self.grid:
            print(x)
    
    # opens the site(row,col), if it is not already open
    def open(self, row: int, col: int) -> None:
        self.grid[row][col] = 1

    # is the site open (row,col)?
    def is_open(self, row: int, col: int) -> bool:
        return self.grid[row][col] != 0

    # is the site full?
    def is_full(self, row: int, col: int) -> bool:
        i, j = row, col
        if i == 0: True 


    # returns the number of open sites
    def number_of_open_sites() -> int:

    # does the system percolate?
    def percolates() -> bool:
