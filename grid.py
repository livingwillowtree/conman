
OFFSETS = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1) 
)
class Grid:
    def __init__(
        self,
        row_count = 80,
        col_count = 80,
        ):

        self.row_count = row_count
        self.col_count = col_count

        self._alive_cells = set()
        
    def edit_cell(self, x, y, state):
        """Add or Delete Cell to Set"""
        if state == 1:
            self._alive_cells.add((x,y))
        else:
            self._alive_cells.discard((x,y))
        # print(f"Cell Added to {x, y}")

    def add_candidates(self, candidates):
        """Add cells to a set for fate evaluation"""
        for x, y in self._alive_cells:
            candidates.add((x, y))
            for dx, dy in OFFSETS:
                candidates.add((x+dx, y+dy))
    
    def count_neighbors(self, x, y):
        """... Did you really have to hover over this?"""
        count = 0
        for dx, dy in OFFSETS:
            if (x+dx, y+dy) in self._alive_cells:
                count += 1
                # print(f"Neighbor in {x+dx, y+dy}")
        return count

    def determine_fate(self, x, y):
        """Playing god over pixels"""
        count = self.count_neighbors(x,y)

        if (x,y) not in self._alive_cells:
            if count == 3:
                return True
        elif count < 2:
            return False
        elif count <= 3:
            return True
        elif count > 3:
            return False

        return False

    def next_gen(self):
        """Determine the the next generation set"""
        next_generation_cells = set()
        candidate_cells = set()

        self.add_candidates(candidate_cells)

        for x, y in candidate_cells:
            is_alive = self.determine_fate(x,y)
            if is_alive:
                next_generation_cells.add((x,y))
                # print(f"{x,y} Should Be Alive")
            # print(f"{x,y} Should Be Dead")

        self._alive_cells = next_generation_cells
        
        # print(f"New gen: {self._alive_cells}")

    def get_grid_data(self):
        """... Did you just hover over this?"""
        return self._alive_cells
    
    def clear_grid(self):
        """... Dude ..."""
        self._alive_cells.clear()
    