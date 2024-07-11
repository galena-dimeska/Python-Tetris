class Colors:

	dark_grey = (204, 204, 255) #color of empty cell
	green = (102, 255, 178)
	red = (255, 153, 204)
	orange = (255, 178, 102)
	yellow = (255, 255, 153)
	purple = (178, 102, 255)
	cyan = (255, 153, 255)
	blue = (51, 153, 255)
	white = (255,255,255) #font color
	pale_blue = (153, 153, 255) #background
	light_blue = (109, 109, 202)


	@classmethod
	def get_cell_colors(cls): 	
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] 
		#the order is important, empty cell has to be at[0]
		
		