# MazeMaker
MazeMaker is a Python script, that can generate Mazes using the randomised
Kruskal algorithm.

``` Python
# Will generate a Maze, which can be accessed as nested Lists using m.field
m = Maze(size=(10, 10))  

# Optionally add entrance and exit
m.field[1][0] = 1
m.field[m.SIZE[0]-2][m.SIZE[1]-1] = 1

# Export the Maze as a PNG using PIL
m.export()
```
