import sys

# Redefine input() to read one line at a time
input = sys.stdin.readline
matrix = [list(map(int, input().split())) for _ in range(5)]
flag_coord = None

# Get flag coordinates
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 1:
            flag_coord = [x, y]

# Count steps to make matrix beautiful
steps_horiztonal = abs(2 - flag_coord[1])
steps_vertical = abs(2 - flag_coord[0])

print(steps_horiztonal + steps_vertical)
