# section_mapping.py
def create_grid(frame_width, frame_height, n_cols, n_rows):
    """
    Create a grid of screen sections.
    Returns a list of dictionaries, each representing a grid cell with boundaries and an id.
    """
    grid = []
    cell_width = frame_width / n_cols
    cell_height = frame_height / n_rows
    for row in range(n_rows):
        for col in range(n_cols):
            cell = {
                'id': row * n_cols + col,
                'row': row,
                'col': col,
                'x_min': col * cell_width,
                'x_max': (col + 1) * cell_width,
                'y_min': row * cell_height,
                'y_max': (row + 1) * cell_height
            }
            grid.append(cell)
    return grid

def get_region_for_point(x, y, grid):
    """
    Given a point (x, y) and a grid, return the cell id where the point lies.
    """
    for cell in grid:
        if cell['x_min'] <= x < cell['x_max'] and cell['y_min'] <= y < cell['y_max']:
            return cell['id']
    return None
