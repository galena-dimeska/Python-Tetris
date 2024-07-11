#empty cells- value of 0
#when the colored blocks are Permanently placed on the grid - the values will be numbers (ex, yellow - 4 to corresponding cells)
# 7 different color of blocks - 1-7 for the colored blocks (0 for empty cells)
import pygame
from colors import Colors

class Grid:
	#initialize the grid 
	def __init__(self):
		self.num_rows = 20
		self.num_cols = 10
		self.cell_size = 30 

		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

		self.colors = Colors.get_cell_colors() #prima lista od boite


	def print_grid(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				print(self.grid[row][column], end = " ") 
			print() 


	def is_inside(self, row, column):
		if row >=0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False


	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False


	def is_row_full(self, row):
		#we need to get every column so can check if Every cell in the row is 0
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False
		return True

	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row][column] = 0

	def move_row_down(self, row, num_rows):
		for column in range(self.num_cols):
			#moves a row in the grid down by the number of completed rows
			#by copying the values of the original row to a new row 
			self.grid[row+num_rows][column] = self.grid[row][column]

			#clearing the original row
			self.grid[row][column] = 0


	def clear_full_rows(self):
		completed = 0

		#iterates through the rows of the grid in REVERSE order, bottom-to-top
		for row in range(self.num_rows - 1 , 0, -1): 
			if self.is_row_full(row):
				self.clear_row
				completed+=1
			elif completed >0:
				self.move_row_down(row, completed)

		return completed


	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0


	def draw(self, screen):
		#drawing each cell of the grid with a specific color
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column] 
				cell_rect = pygame.Rect(column*self.cell_size +11, row*self.cell_size +11, self.cell_size -1, self.cell_size -1) 
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)




