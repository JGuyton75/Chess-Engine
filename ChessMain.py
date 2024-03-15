#
# Main Driver File
# Handles user input and displays the current GameState object.
#

import pygame as p
import ChessEngine

p.init()
WIDTH = HEIGHT = 512            # 400 could work.
DIMENSION = 8                   # 8x8 chess board.
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15                    # Animations
IMAGES = {}

# Intialize a global dictionary of images. Called ONCE in main.
def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wR', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bR', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Chess/Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # We can access an image by using the dictionary, 'IMAGES['wP']' gives us an image.
        
# Main driver for code. Maintains user input, updates graphics.
def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()                    # Only do this ONCE.
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# Controls Graphics within current GameState.
def drawGameState(screen, gs):
    drawBoard(screen)               # Draw Squares on Board
    drawPieces(screen, gs.board)    # Draw pieces on board. (Later: Highlight selected piece, move suggest)


# Draw Squares on board
def drawBoard(screen):
    colors = [p.Color("light gray"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            # Highlights can go here. 

# Draw pieces on board using current GameState.board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':       # Not empty.
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
        main()