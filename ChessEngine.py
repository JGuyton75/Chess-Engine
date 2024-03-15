#
# Stores all information about the current state of a chess game.
# Also determines vaild moves at the current state. Will keep a move log.
#
class GameState():
    def __init__(self):
        self.board = [                                          # 8x8 List, each element has 2 characters. The first
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],   # character is the color of the piece. "b" or "w".
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],   # The second character is the type of piece. "Q, P, K".
            ["--", "--", "--", "--", "--", "--", "--", "--"],   # "--" is empty board space.
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.movelog = []