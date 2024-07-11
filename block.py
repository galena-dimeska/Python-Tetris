from colors import Colors
import pygame
from position import Position

class Block:
	def __init__(self, id):
		self.id = id 
		self.cells = {} 
		self.cell_size = 30 
		self.rotation_state = 0

		self.colors = Colors.get_cell_colors()

		self.row_offset = 0
		self.column_offset = 0


	def move(self, rows, columns):
		self.row_offset += rows 
		self.column_offset += columns 

	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state]
		
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)

		return moved_tiles


	def rotate_clockwise(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells): 
			self.rotation_state = 0

	def rotate_counter_clockwise(self):
		self.rotation_state -= 1
		if self.rotation_state == -1: 
			self.rotation_state = len(self.cells) - 1 


	def draw(self, screen, offset_x, offset_y): 

		cell_positions = self.get_cell_positions()

		for cell_position in cell_positions:
			cell_rect = pygame.Rect(
				offset_x + cell_position.column*self.cell_size, 
				offset_y + cell_position.row*self.cell_size, 
				self.cell_size -1, self.cell_size -1)

			pygame.draw.rect(screen, self.colors[self.id], cell_rect)







