import pygame, sys, random, math
from pygame.locals import *

# Global variables
SCREENSIZE = (255, 275)
CAPTION = "Click Tester"
ROWS = 10
COLUMNS = 10
WIDTH = 20
HEIGHT = 20
MARGIN = 5
FPS = 60
POINTS = 0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 153, 51)
BLUE = (0, 102, 255)



def main():
	global FPSCLOCK, DISPLAYSURF, POINTS, FONT
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode(SCREENSIZE)
	FONT = pygame.font.Font(None, 25)

	# Mouse coordinates
	mousex = 0
	mousey = 0

	moves = 0
	frameCount = 0

	pygame.display.set_caption(CAPTION)

	newBoard = generateBoard()
	# Main game loop
	while True:
		frameCount += 1
		mouseClicked = False
		# event handling
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True

		# Game logic goes here
		boxx, boxy = getBoxAtPixel(mousex, mousey)
		if (boxx != None and boxy != None) and mouseClicked:
			# The mouse is currently over a box
			if isGreen(newBoard, boxx, boxy) == True:
				POINTS += 1
				frameCount = 0
				newBoard = generateBoard()

			moves += 1
		if timer(moves) <= frameCount // FPS:
			newBoard = generateBoard()
			frameCount = 0
		# Drawing stuff goes here
		clearBoard()
		drawBoard(newBoard)
		output_string = "Points: " + str(POINTS)
		text = FONT.render(output_string, True, BLACK)
		DISPLAYSURF.blit(text, [5, 255])
		
		# Update screen
		pygame.display.update()
		FPSCLOCK.tick(FPS)


# Various Functions go here

def clearBoard():
	DISPLAYSURF.fill(WHITE)

def generateBoard():
	grid = []
	for row in range(ROWS):
	    # Add an empty array that will hold each cell
	    # in this row
	    grid.append([])
	    for column in range(COLUMNS):
	        grid[row].append(0)  # Append a cell
	grid[random.randint(0, ROWS-1)][random.randint(0, COLUMNS-1)] = 1
	return grid

def drawBoard(newBoard):
	for row in range(ROWS):
	  for column in range(COLUMNS):
	      color = BLUE
	      if newBoard[row][column] == 1:
	          color = GREEN
	      pygame.draw.rect(DISPLAYSURF,
	                       color,
	                       [(MARGIN + WIDTH) * column + MARGIN,
	                        (MARGIN + HEIGHT) * row + MARGIN,
	                        WIDTH,
	                        HEIGHT])

def timer(moves):
	operator = - 0.05
	time = math.exp(operator * moves)
	return time

def leftTopCoordsOfBox(boxx, boxy):
	left = boxx * (WIDTH + MARGIN)
	top = boxy * (WIDTH + MARGIN)
	return (left, top)

def getBoxAtPixel(x, y):
	for boxx in range(ROWS):
		for boxy in range(COLUMNS):
			left, top = leftTopCoordsOfBox(boxx, boxy)
			boxRect = pygame.Rect(left, top, WIDTH, HEIGHT)
			if boxRect.collidepoint(x,y):
				return(boxx, boxy)
	return (None, None)

def isGreen(board, boxx, boxy):
	if board[boxy][boxx] == 1:
		return True
	else:
		return False

# Call main function

if __name__ == '__main__':
	main()