import random
import PIL.Image
import PIL.ImageDraw

class Maze:
	def __init__(self, size=(5, 5), seed=None):
		""" Generates a Maze

		Creates and generates a maze using the randomised Kruskal algorithm.

		Args:
			size: Tuple, X and Y number of "rooms" in maze
			seed: String/Int, The seed for the random generator
		"""
		random.seed(seed)

		self.SIZE = tuple(map(lambda x: x*2+1, size))  # Take size *2+1

		self.cells = []  # The "Rooms" of the maze
		self.walls = []  # The Walls in the maze
		self.field = []  # A 2D List of each position of the maze

		# Create Waffle and fill Cells and Walls
		for x in range(self.SIZE[1]):
			self.field.append([])
			for y in range(self.SIZE[0]):
				if x * y % 2:
					self.field[x].append(1)
					self.cells.append([(x, y)])
				else:
					self.field[x].append(0)
					if (
					0 < x < self.SIZE[0]-1 and
					0 < y < self.SIZE[1]-1 and
					not (x+1) * (y+1) % 2):
						self.field[x][y] = 2
						self.walls.append((x, y))

		self.__generate()

	def __generate(self):
		""" Does the generation process """

		def find_set(cell):
			""" Finds the set, in which the Cell is contained in. """
			for x in self.cells:
				if cell in x:
					return x

		random.shuffle(self.walls)

		while len(self.cells) > 1:
			wall_x, wall_y = self.walls[0]

			if wall_x % 2:
				cell1 = (wall_x, wall_y + 1)
				cell2 = (wall_x, wall_y - 1)
			else:
				cell1 = (wall_x + 1, wall_y)
				cell2 = (wall_x - 1, wall_y)
			
			set1 = find_set(cell1)
			set2 = find_set(cell2)

			if set1 != set2:
				self.field[wall_x][wall_y] = 1
				a = self.cells.pop(self.cells.index(set1))
				b = self.cells.pop(self.cells.index(set2))
				self.cells.append(a+b)
			self.walls.pop(0)

	def export(self, cell_width=9, wall_width=1):
		""" Exports the maze to a PNG file

		Args:
			cell_width: The width of the cells 
			wall_width: The width of the walls
		"""
		img_size = (
		self.SIZE[0] // 2 * cell_width
		+ (self.SIZE[0] // 2 + 1) * wall_width,
		self.SIZE[1] // 2 * cell_width
		+ (self.SIZE[1] // 2 + 1) * wall_width)

		img = PIL.Image.new("1", img_size)
		dimg = PIL.ImageDraw.Draw(img)

		posX = 0
		posY = 0
		for x in range(self.SIZE[0]):
			width = cell_width if x % 2 else wall_width
			posY = 0
			for y in range(self.SIZE[1]):
				height = cell_width if y % 2 else wall_width
				dimg.rectangle((posX, posY, posX+width, posY+height), self.field[x][y]!=1)
				posY += height
			posX += width
		
		img.save("result.png")

if __name__ == "__main__":
	m = Maze((100, 100), 0)
	m.field[1][0] = 1
	m.field[m.SIZE[0]-2][m.SIZE[1]-1] = 1
	m.export()

