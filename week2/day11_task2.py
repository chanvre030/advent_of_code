import numpy as np

grid = np.array(list(list(line) for line in open("input_day11.txt", "r").read().split("\n")), dtype=int)
big_flash = False
i = 0
while not big_flash:
    i += 1
    grid += 1
    while np.max(grid) > 9:
        grid = np.where(grid > 9, -1, grid)
        flashed = np.where(grid == -1)
        for x, y, in zip(flashed[0], flashed[1]):
            for xx in range(x - 1, x + 2):
                for yy in range(y - 1, y + 2):
                    if not (xx == x and yy == y) and not (xx < 0 or yy < 0):
                        try:
                            if grid[xx, yy] > -1:
                                grid[xx, yy] += 1
                        except IndexError:
                            pass
        grid = np.where(grid == -1, grid - 1, grid)
    grid = np.where(grid < 0, 0, grid)
    if np.sum(grid) == 0:
        big_flash = True
print("rounds until big flash:", i)
