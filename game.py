import pygame
from grid import Grid
from blocks import *
import random

class Game:
	def __init__(self):
		self.grid = Grid()

		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()

		self.game_over = False

		self.score = 0
		self.high_score = 0
		self.load_highscore()

		self.rotate_sound = pygame.mixer.Sound("Sounds/Sounds_rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("Sounds/Sounds_clear.ogg")

		pygame.mixer.music.load("Sounds/music.ogg")
		pygame.mixer.music.set_volume(0.15)
		pygame.mixer.music.play(-1) 


	def update_score(self, lines_cleared, moved_down_points):
		#100 points for a single line cleared, 300 for 2, 500 for 3, 1 for every block moved down
		if lines_cleared == 1:
			self.score += 100
			self.check_for_high_score()
		elif lines_cleared == 2:
			self.score += 300
			self.check_for_high_score()
		elif lines_cleared == 3:
			self.score += 500
			self.check_for_high_score()
		elif lines_cleared == 4:
			self.score += 1000
			self.check_for_high_score()
		self.score +=  moved_down_points
		self.check_for_high_score()


	#returning a random block
	#in tetris a block from each type has to spawn randomly once before being allowed to reappear
	def get_random_block(self):

		if len(self.blocks)==0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

		block = random.choice(self.blocks) 
		self.blocks.remove(block) 
		return block


	def move_left(self):
		self.current_block.move(0,-1) 

		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0,1)


	def move_right(self):
		self.current_block.move(0,1)

		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0,-1)


	def move_down(self):
		self.current_block.move(1,0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1,0)
			self.lock_block()


	def rotate_clockwise(self):
		self.current_block.rotate_clockwise()
		if self.block_inside() == False  or self.block_fits() == False:
			self.current_block.rotate_counter_clockwise() 
		else:
			self.rotate_sound.play()

	def rotate_counter_clockwise(self):
		self.current_block.rotate_counter_clockwise()
		if self.block_inside() == False  or self.block_fits() == False:
			self.current_block.rotate_clockwise() 
		else:
			self.rotate_sound.play()


	#when any piece of the block touches the bottom of the screen we need to lock it in place so that it can't be moved anymore
	def lock_block(self): 
		block_positions = self.current_block.get_cell_positions()
		#for each cell of the block, we will store its id number instead of 0 in the positions of the cells
		for cell_position in block_positions:
			self.grid.grid[cell_position.row][cell_position.column] = self.current_block.id

		#now we need to spawn a new block in the game
		self.current_block = self.next_block
		self.next_block = self.get_random_block()

		#return the number of rows cleared
		rows_cleared = self.grid.clear_full_rows() 
		if rows_cleared>0:
			self.clear_sound.play()
		
		self.update_score(rows_cleared,0)
		self.check_for_high_score()

		#the game ends if the newly spawned block can't move down anymore
		if self.block_fits() == False:
			self.game_over = True


	def reset(self):
		#we need to clear the grid
		self.grid.reset()

		#we need to select a new current block and next block
		#we also need to recreate the list of blocks
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()

		#when we reset the game the score should be 0
		self.score = 0 


	def block_fits(self):
		block_positions = self.current_block.get_cell_positions()

		for cell_position in block_positions:
			if self.grid.is_empty(cell_position.row, cell_position.column) == False:
				return False

		return True
		#if they're all available the block can move there


	def block_inside(self):
		block_positions = self.current_block.get_cell_positions() 
		for cell_position in block_positions:
			if self.grid.is_inside(cell_position.row, cell_position.column) == False:
				return False

		return True


	def draw(self, screen):
		self.grid.draw(screen)
		#adding an offset for drawing the current block
		self.current_block.draw(screen, 11, 11)
		
		#but the I and O block arent centered so we have to check the id of the block before drawing

		if self.next_block.id == 3: # I block
			self.next_block.draw(screen, 255, 290) 
		elif self.next_block.id == 4: #O block
			self.next_block.draw(screen, 255, 280) 
		else:
			self.next_block.draw(screen, 270, 270) 


	def check_for_high_score(self):
		if self.score>self.high_score:
			self.high_score = self.score

			with open("highscore.txt", "w") as file: 
				file.write(str(self.high_score))


	def load_highscore(self):
		try:
			with open("highscore.txt", "r") as file: 
			#so r za citanje samo
				self.high_score = int(file.read())
		except FileNotFoundError:
			self.high_score = 0


