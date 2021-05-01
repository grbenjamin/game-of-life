from random import *

ALIVE_CELL = 1
DEAD_CELL = 0

class Board:
    __slots__ = ['_values', '_width', '_height', '_len']

    def __init__(self, width = 0, height = 0, random = True):
        self._values = []
        self._len = 0
        self._width = width
        self._height = height
        if width > 0 and height > 0:
            if not random:
                self.fill_values(0)
            else:
                self.fill_values_randomly()

    def append(self, value):
        self._values.append(value)

    def fill_values(self, value = 0):
        """ fills the board with the value given """
        if self.is_empty():
            for row in range(self._height):
                # add a new row
                self.append([])
                for column in range(self._width):
                    # append value to the row
                    self._values[row].append(value)
                    self._len += 1
        else:
            for row in range(self._height):
                for column in range(self._width):
                    self._values[row][column] = value

        # make sure the board was filled
        assert not self.is_empty(), 'No elements were added'

        return self._values

    def fill_values_randomly(self):
        """ fills the board randomly with either a 0 or a 1 """
        for row in range(self._height):
            # add a new row
            self.append([])
            for column in range(self._width):
                # assign random values to every number and append that to the row
                rand_number = random()
                rand_number = 1 if rand_number >= 0.7 else 0
                self._values[row].append(rand_number)
                self._len += 1

        # make sure the board was filled
        assert not self.is_empty(), 'No elements were added'

        return self._values

    def change_pos_value(self, row, column, value):
        self._values[row - 1][column - 1] = value

    def next_board_state(self):
        """ calculates and returns a new board with updated values """
        if not self.is_empty():
            new_board = Board(self._width, self._height)
            for row in range(self._height):
                for column in range(self._width):
                    # get the cell we're working on
                    cell = self._values[row][column]
                    # count its neighbors
                    neighbors = self.count_neighbors(row, column)
                    if cell == ALIVE_CELL:
                        if neighbors == 0 or neighbors == 1:
                            cell = DEAD_CELL
                        if neighbors == 2 or neighbors == 3:
                            cell = ALIVE_CELL
                        if neighbors > 3:
                            cell = DEAD_CELL
                    else:
                        if neighbors == 3:
                            cell = ALIVE_CELL

                    new_board.change_pos_value(row + 1, column + 1, cell)

        return new_board

    def count_neighbors(self, row, column):
        values = 0

        first_row = row == 0
        in_between_rows = row > 0 and row < self._height - 1
        last_row = row == self._height - 1
        in_between_columns = column > 0 and column < self._width - 1

        if column == 0:
            # first element of each row
            if first_row:
                # calculate 3 corners
                if self._values[row][column + 1] == 1:       # right
                    values += 1
                if self._values[row + 1][column] == 1:       # down
                    values += 1
                if self._values[row + 1][column + 1] == 1:   # down right
                    values += 1
            elif in_between_rows:
                # calculate 5 corners
                if self._values[row - 1][column] == 1:       # up
                    values += 1
                if self._values[row - 1][column + 1] == 1:   # up right
                    values += 1
                if self._values[row][column + 1] == 1:       # right
                    values += 1
                if self._values[row + 1][column + 1] == 1:   # down right
                    values += 1
                if self._values[row + 1][column] == 1:       # down
                    values += 1
            else:
                # last row. calculate 3 corners
                if self._values[row - 1][column] == 1:       # up
                    values += 1
                if self._values[row - 1][column + 1] == 1:   # up right
                    values += 1
                if self._values[row][column + 1] == 1:       # right
                    values += 1

        if in_between_columns:
            # calculate 5 corners
            if first_row:
                if self._values[row][column - 1] == 1:      # left
                    values += 1
                if self._values[row + 1][column - 1] == 1:  # down left
                    values += 1
                if self._values[row + 1][column] == 1:      # down
                    values += 1
                if self._values[row + 1][column + 1] == 1:  # down right
                    values += 1
                if self._values[row][column + 1] == 1:      # right
                    values += 1
            elif last_row:
                if self._values[row][column - 1] == 1:      # left
                    values += 1
                if self._values[row - 1][column - 1] == 1:  # up left
                    values += 1
                if self._values[row - 1][column] == 1:      # up
                    values += 1
                if self._values[row - 1][column + 1] == 1:  # up right
                    values += 1
                if self._values[row][column + 1] == 1:      # right
                    values += 1

        if column == self._width - 1:
            # last element of each row
            if first_row:
                # calculate 3 corners
                if self._values[row][column - 1] == 1:       # left
                    values += 1
                if self._values[row + 1][column - 1] == 1:   # down left
                    values += 1
                if self._values[row + 1][column] == 1:       # down
                    values += 1
            elif in_between_rows:
                # calculate 5 corners
                if self._values[row - 1][column] == 1:       # up
                    values += 1
                if self._values[row - 1][column - 1] == 1:   # up left
                    values += 1
                if self._values[row][column - 1] == 1:       # left
                    values += 1
                if self._values[row + 1][column - 1] == 1:   # down left
                    values += 1
                if self._values[row + 1][column] == 1:       # down
                    values += 1
            else:
                # last row. calculate 3 corners
                if self._values[row - 1][column] == 1:       # up
                    values += 1
                if self._values[row - 1][column - 1] == 1:   # up left
                    values += 1
                if self._values[row][column - 1] == 1:       # left
                    values += 1
        
        if in_between_rows and in_between_columns:
            if self._values[row][column - 1] == 1:           # left
                values += 1
            if self._values[row][column + 1] == 1:           # right
                values += 1
            if self._values[row - 1][column] == 1:           # up
                values += 1
            if self._values[row + 1][column] == 1:           # down
                values += 1
            if self._values[row - 1][column - 1] == 1:       # up left
                values += 1
            if self._values[row - 1][column + 1] == 1:       # up right
                values += 1
            if self._values[row + 1][column - 1] == 1:       # down left
                values += 1
            if self._values[row + 1][column + 1] == 1:       # down right
                values += 1

        return values
    
    def render(self):
        """ renders the board to the terminal """
        assert not self.is_empty(), 'No elements'

        print('-' * (self._width + 2)) # top corners
        
        for row in range(self._height):
            for column in range(self._width):
                if column == 0: # left corners
                    print('|', end = '')

                # print a hash symbol if a cell is alive
                print('#' if self._values[row][column] == 1 else ' ', end = '')

                if column == self._width - 1: # right corners
                    print('|', end = '')
            print('\n', end = '')

        print('-' * (self._width + 2)) # bottom corners

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def is_empty(self):
        #return self._width == 0 or self._height == 0
        return self._len == 0

    def clear(self):
        self._values.clear()

    def copy(self):
        values = self._values.copy()

    def update(self):
        temp = Board(self._width, self._height, False)
        self.render()
        temp.render()

    def __len__(self):
        return self._len

    def __repr__(self):
        return ('[' + ', '.join(repr(x) for x in self._values) + ']')