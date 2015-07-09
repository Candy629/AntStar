from antstar.Grid import Grid

grid_text = """
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 X 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 S 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""

grid = Grid.from_string(grid_text)
#
# wall_positions = [
#
#     (6, 5), (7, 5), (8, 5),
#     (6, 6),         (8, 6), (9, 6),
#     (6, 7), (7, 7),         (9, 7), (10, 7),
#             (7, 8), (8, 8),         (10, 8), (11, 8),
#                     (8, 9), (9, 9),
#                             (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10),
#                                      (10, 11),                                         (15, 11),
#                                      (10, 12),                                         (15, 12),
#                                      (10, 13),                                         (15, 13),
#                                      (10, 14),
#                                      (10, 15), (11, 15), (12, 15), (13, 15)
# ]
#
# grid = Grid(20, 20, start=(18, 18), end=(1, 1))
# grid.add_wall(wall_positions)

grid.print()
