# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    # UL = "  "; UM = "  "; UR = "  "
    # ML = "  "; MM = "  "; MR = "  "
    # LL = "  "; LM = "  "; LR = "  "
    # def printBoard():

    #     print("    |    |    ")
    #     print(" " + UR + " | " + UM + " | " + UR + " ")
    #     print("____|____|____")
    #     print("    |    |    ")
    #     print(" " + MR + " | " + MM + " | " + MR + " ")
    #     print("____|____|____")
    #     print(" " + LR + " | " + LM + " | " + LR + " ")
    #     print("    |    |    ")
    
    # printBoard()
    def __init__(self) -> None:
        self.board = ['*'] * 9

    def __str__(self) -> str:
        s = ""
        for x in [0, 3, 6]:
            s += self.board[x + 0] + " " + self.board[x + 1] + " " + self.board[x + 2] + "\n"
        return s
    
    def make_move(self, player, pos) -> bool:
        if (pos < 0 or pos > 8 or self.board[pos] != '*'):
            return False
        self.board[pos] = player
        return True
    
    def has_won(self, player) -> bool:
        for x in [0, 3, 6]:
        #     print(" horz line")
        #     print(self.board[x])
        #     print(self.board[x+1])
        #     print(self.board[x+2])
        #     print("\n")
            if (self.board[x] == player and self.board[x + 1] == player and self.board[x + 2] == player):
                return True
        # for x in [0, 1, 2]:
        #     print(" vert line")
        #     print(self.board[x])
        #     print(self.board[x+3])
        #     print(self.board[x+6])
        #     print("\n")
            if (self.board[x] == player and self.board[x + 3] == player and self.board[x + 6] == player):
                return True
        if (self.board[0] == player and self.board[4] == player and self.board[8] == player):
            return True
        if (self.board[2] == player and self.board[4] == player and self.board[6] == player):
            return True
        return False
    
    
    def game_over(self) -> bool:
        filled = True
        for x in self.board:
            if x == '*':
                filled = False
        if self.has_won("X") or self.has_won("O"):
            return True
        return filled
    
    def clear(self) -> None:
        self.board = ['*'] * 9


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    print(brd.board)
    print(brd)
    brd.make_move("X", 0)
    brd.make_move("O", 3)
    brd.make_move("O", 4)
    print(brd)
    print(brd.has_won("X"))

    assert brd.game_over() == False, "Game falsly over. Assert 1"

    brd.make_move("X", 1)
    brd.make_move("O", 8)
    brd.make_move("X", 2)
    print(brd)
    print(brd.has_won("X"))

    assert brd.has_won("X") == True, "Has won X is not true. Asset 2"
    assert brd.has_won("O") == False, "Has won O is not false. Assert 3"
    assert brd.game_over() == True, "Game over is wrongly false. Assert 4"

    brd.clear()
    print(brd.board)

    assert brd.game_over() == False, "5"

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False, "6"
    assert brd.has_won("O") == True, "7"
    assert brd.game_over() == True, "8"

    print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()
