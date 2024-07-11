import pygame, sys
from game import Game
from colors import Colors


pygame.init() 

#creating a font for the score and game over text
title_font = pygame.font.Font(None, 40) 

score_surface = title_font.render("Score", True, Colors.white) 
score_rect = pygame.Rect(320, 55, 170, 60) 

next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)

high_score_text_surface = title_font.render("High Score", False, Colors.white)
high_score_rect = pygame.Rect(320, 485, 170, 60) 

game_over_surface = title_font.render("Game Over :(", True, Colors.white)

screen = pygame.display.set_mode((500,620)) 

pygame.display.set_caption("Python Tetris") #giving the screen a name

clock = pygame.time.Clock() 

game = Game()

#we need a user event so that the blocks can fall
#event will be triggered every time a block's position needs to be updated
GAME_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(GAME_UPDATE, 200) 


while True: 
	for event in pygame.event.get(): 	
		if event.type == pygame.QUIT: 
			pygame.quit() 
			sys.exit() 	

		if event.type == pygame.KEYDOWN:

			if game.game_over == True:
				#we need to restart the game
				game.game_over= False
				game.reset()

			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0,1)
			if event.key == pygame.K_x and game.game_over == False:
				game.rotate_clockwise()
			if event.key == pygame.K_z and game.game_over == False:
				game.rotate_counter_clockwise()

		#to make the blocks fall down		
		#we added game_over = false so that if the game ends, blocks won't be able to move down anymore
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()


	#Drawing

	score_value_surface = title_font.render(str(game.score), True, Colors.white)
	formatted_high_score = str(game.high_score)
	high_score_surface = title_font.render(formatted_high_score, False, Colors.white)

	screen.fill(Colors.pale_blue) 
	
	screen.blit(score_surface, (365, 20, 50, 50)) 
	screen.blit(next_surface, (375, 180, 50, 50))
	screen.blit(high_score_text_surface, (330, 450, 50, 50))
	

	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))

	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	
	pygame.draw.rect(screen, Colors.light_blue, high_score_rect, 0, 10) 
	screen.blit(high_score_surface, high_score_surface.get_rect(centerx = high_score_rect.centerx, centery = high_score_rect.centery))

	if game.game_over == True:
		screen.blit(game_over_surface, (317, 570, 50, 50))

	game.draw(screen)

	pygame.display.update()
	
	clock.tick(60) 
