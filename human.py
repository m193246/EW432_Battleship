
import ship, game_board, sprites
from random import randint
from typing import List, Tuple, Optional


class Human:
    """ A human player"""

    def __init__(self):

        # list of ship objects
        self._my_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._my_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates
        self._my_hit: List[Tuple[int, int]] = []
        # list of ship objects
        self._sunk_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._their_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates
        self._their_hits: List[Tuple[int, int]] = []

        # the board matrix is a 10x10 structure with
        # pointers to ship objects. Initialize to all
        # None values- no ships are on the board
        self._board_matrix: List[List[Optional[ship.Ship]]] = [[None] * 10 for _ in range(10)]

        # set to True if all opponent's ships are sunk
        self.complete: bool = False

    def initialize(self):
        """ Create a valid ship layout
        This function populates
        _my_ships and _board_matrix

        Ship Type  | Length
        -----------|-------
        Carrier    |   5
        Battleship |   4
        Cruiser    |   3
        Submarine  |   3
        Destroyer  |   2

        * the ship type is just FYI, it is not used in the game *
        """

        for ship_length in [5, 4, 3, 3, 2]:

            # --------- BEGIN YOUR CODE ----------
            error = True
            while error is True:

                # 1.) create ship of the given length at a random (row,col)
                #     position either horizontal or vertical
                orient = randint(0, 1)
                if orient == 1:
                    row = randint(0, 9)
                    column = randint(0, 10 - ship_length)

                else:
                    row = randint(0, 10 - ship_length)
                    column = randint(0, 9)

                my_ship = ship.Ship(ship_length, row, column, orient)



                # 2.) check if this conflicts with any of the other ships by
                #     by making sure that every entry in _board_matrix is None

                valid = []

             # 2b.) If the ship is not valid, retry step 1
                if orient == 1:
                    if self._board_matrix[row][column - ship_length] is None:
                        valid.append('Yes')
                    else:
                        valid.append('No')

                else:
                    if self._board_matrix[row - ship_length][column] is None:
                        valid.append('Yes')
                    else:
                        valid.append('No')


                # 3.) If the ship is valid set the appropriate elements _board_matrix array
                #     equal to the ship
                # Example: to place a vertical destroyer at C2:
                if 'No' not in valid:
                        for n in range(1, ship_length - 1):
                            if orient == 1:
                                self._board_matrix[row + n][column] = my_ship
                            else:
                                self._board_matrix[row][column + n] = my_ship

                self._my_ships.append(my_ship)
                error = False
            # --------- END YOUR CODE ----------

    def print_board(self):
        """
        Print the player's board as text, useful for debugging
        """

        print("=" * 10)
        for row in self._board_matrix:
            for entry in row:
                if entry is None:
                    print("_", end="")
                else:
                    print(entry.length, end="")
            print("")
        print("=" * 10)

    def draw(self,
             my_board: game_board.GameBoard,
             their_board: game_board.GameBoard):

        """ Add sprites to the game board's to indicate
        ship positions, guesses, hits, etc """

        for my_ship in self._my_ships:
            my_ship.draw(my_board)
