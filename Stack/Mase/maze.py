# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from pprint import pprint

class Maze :
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = " *"
    PATH_TOKEN = " x"
    TRIED_TOKEN = " o"

    # Creates a maze object with all cells marked as open.
    def __init__( self, num_rows, num_cols ):
        self._mazeCells = Array2D( num_rows, num_cols )
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def num_rows( self ):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols( self ):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition( row, col )

    # Sets the exit cell position.
    def setExit( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition( row, col )

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath( self ):
        start = self._startCell.row, self._startCell.col
        end = self._exitCell.row, self._exitCell.col
        lst = []
        for row in self._mazeCells.rows: # creates list of coors to work with
            temp = []
            for item in row:
                if item is not None:
                    temp.append('*')
                else:
                    temp.append(' ')
            lst.append(temp)
        lst[start[0]][start[1]] = 'S'
        lst[end[0]][end[1]] = 'E'

        def search(row, col): # searches for the path using recursion
            if lst[row][col] == 'E':
                return True
            elif lst[row][col] == '*':
                return False
            elif lst[row][col] == 'o':
                return False
            lst[row][col] = 'o'
            if ((row < len(lst) - 1 and search(row + 1, col)) or (col > 0 and search(row, col - 1))
                or (row > 0 and search(row - 1, col)) or (col < len(lst) - 1 and search(row, col + 1))):
                pprint(lst)
                return True
            return False

        return True if search(start[0], start[1]) else False

    # Resets the maze by removing all "path" and "tried" tokens.
    def reset( self ):
        pass

    # Prints a text-based representation of the maze.
    def draw( self ):
        lst = []
        text = ''
        self._mazeCells.rows[self._startCell.row][self._startCell.col] = ' S'
        self._mazeCells.rows[self._exitCell.row][self._exitCell.col] = ' E'
        for row in self._mazeCells.rows:
            temp = []
            for item in row:
                if item is not None:
                    temp.append('* ')
                    text += item
                else:
                    text += '  '
                    temp.append(' ')
            lst.append(temp)
            text += '\n'
        return text

    # Returns True if the given cell position is a valid move.
    def _validMove( self, row, col ):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound( self, row, col ):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried( self, row, col ):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath( self, row, col ):
        self._mazeCells[row, col] = self.PATH_TOKEN

# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__( self, row, col ):
        self.row = row
        self.col = col