from algorithms.find_union.quick_union_find_weighted import QuickUnionFind

class Percolation:
    # create n by n grid, with all sides initially blocked
    def __init__(self, n: int):
        self.gridsize = n
        self.grid_squared = n*n
        self.grid = [[False]*(n) for x in range(n)]
        self.wqf_grid = QuickUnionFind(self.grid_squared + 2) # with virtual top and bottom
        self.wqf_full = QuickUnionFind(self.grid_squared + 1) # with only virtual top
        self.virtual_bottom = self.grid_squared + 1
        self.virtual_top = self.grid_squared
        self.open_sites = 0


    def showgrid(self) -> None:
        for x in self.grid:
            print(x)

    def validate_site(self, row: int, col: int) -> None:
        if not self.is_on_grid(row, col):
            raise IndexError
    
    def is_on_grid(self, row: int, col: int) -> bool:
        shift_row = row - 1
        shift_col = col - 1
        return shift_row >=0 and shift_col >= 0 \
            and shift_col < self.gridsize and shift_row < self.gridsize
    
    # opens the site(row,col), if it is not already open
    def open(self, row: int, col: int) -> None:
        self.validate_site(row, col)
        shift_row = row - 1
        shift_col = col - 1
        flat_index = self.flatten_grid(row, col)
        
        if self.is_open(row, col):
            return 

        self.grid = 

    # is the site open (row,col)?
    def is_open(self, row: int, col: int) -> bool:
        self.validate_site(row, col)
        return self.grid[row-1][col-1]

    # is the site full?
    def is_full(self, row: int, col: int) -> bool: # 1,6
        i, j = row, col
        if (self.n < i <= 0) and (self.n < j <= 0):
            if self.is_open(i, j) and i == 0: 
                return True
            self.is_full(i-1,j)
            self.is_full(i+1,j)
            self.is_full(i,j-1)
            self.is_full(i,j+1)

        return False
        
    def flatten_grid(self, row: int, col: int) -> int:
        return self.gridsize * (row-1) + col


    # returns the number of open sites
    def number_of_open_sites() -> int:

    # does the system percolate?
    def percolates() -> bool:
