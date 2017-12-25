from Domain import Square
from prettytable import PrettyTable
import copy


class GameSimulation:

    """ The  class which simulates the game """
    def __init__(self):
        self._board = [[Square() for j in range(7)] for i in range(6)]
    def __str__(self):
        t = PrettyTable(['0', '1', '2', '3', '4', '5', '6'])
        t.valign = "b"
        t.border = True
        for line in self._board:
            t.add_row(line)
        return str(t)

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self,new_board):
        self._board=new_board


    def available(self):
        """
        Checks the available positions to move
        :return: a list of (x,y) tuples of positions
        """
        available_list = []
        for j in range(7):
            for i in range(6):
                if self._board[i][j].empty is False:
                    if i == 0:
                        break
                    else:
                        available_list.append((i-1, j))
                        break
                elif i == 5 and self._board[i][j].empty:
                    available_list.append((5, j))
        return available_list

    def make_move(self, type_string, x, y):
        """

        :param type_string: Represents a string either yellow or red -> the move
        :param x: represents the x coordinate -> line position , an int
        :param y: represents the y coordinate -> column position, an int
        :return: True if successfull or raises error
        """

        if (x, y) not in self.available():
            raise GameError('Not an available move! ')
        if (x < 0 or x > 5) or (y < 0 or y > 6):
            raise GameError('Position out of range! ')
        if type_string == 'red':
            self._board[x][y].red = True
            return True
        elif type_string == 'yellow':
            self._board[x][y].yellow = True
            return True
        else:
            raise GameError('Not an available move! ')

    def check_diag1(self, choice):
        """
        Checks if a game is won by diagonal NE->SW
        :param choice: a tupple of int representing the last move
        :return: True if won by last move, False if not
        """
        x = choice[0]
        y = choice[1]
        ddrpct = 6 - y
        dsuspct = x
        djospct = 5 - x
        dstpct = y
        a = x - min(ddrpct, dsuspct, 3)
        b = x + min(djospct, dstpct, 3)
        j = y + min(ddrpct, dsuspct, 3)
        for i in range(a, b - 2, 1):
            if self._board[i][j].red:
                if self._board[i + 1][j - 1].red and self._board[i + 2][j - 2].red and self._board[i + 3][j - 3].red:
                    return True
            if self._board[i][j].yellow:
                if self._board[i + 1][j - 1].yellow and self._board[i + 2][j - 2].yellow and self._board[i + 3][j - 3].yellow:
                    return True
            j -= 1
        return False

    def check_diag2(self, choice):
        """
        Checks if a game is won by diagonal SE->NW
        :param choice: a tupple of int representing the last move
        :return: True if game was won by last move, false if not
        """
        x = choice[0]
        y = choice[1]
        ddrpct = 6 - y
        dsuspct = x
        djospct = 5 - x
        dstpct = y
        a = x - min(dsuspct, dstpct, 3)
        b = x + min(djospct, ddrpct, 3)
        j = y - min(dsuspct, dstpct, 3)
        for i in range(a, b - 2, 1):
            if self._board[i][j].red:
                if self._board[i + 1][j + 1].red and self._board[i + 2][j + 2].red and self._board[i + 3][j + 3].red:
                    return True
            if self._board[i][j].yellow:
                if self._board[i + 1][j + 1].yellow and self._board[i + 2][j + 2].yellow and self._board[i + 3][j + 3].yellow:
                    return True
            j += 1
        return False

    def check_line(self, choice):
        """
        Checks the line which contains the last choice for a win
        :return: True if game won or false otherwise
        """
        x = choice[0]
        for j in range(4):
            if self._board[x][j].red:
                if self._board[x][j + 1].red and self._board[x][j + 2].red and self._board[x][j + 3].red:
                    return True
            if self._board[x][j].yellow:
                if self._board[x][j + 1].yellow and self._board[x][j + 2].yellow and self._board[x][j + 3].yellow:
                    return True
        return False

    def check_column(self, choice):
        """
        Checks the column which contains the last move
        :param choice: tuple of int representing the last move
        :return: True if game won or false otherwise
        """
        y = choice[1]
        for i in range(3):
            if self._board[i][y].red:
                if self._board[i + 1][y].red and self._board[i + 2][y].red and self._board[i + 3][y].red:
                    return True
            if self._board[i][y].yellow:
                if self._board[i + 1][y].yellow and self._board[i + 2][y].yellow and self._board[i + 3][y].yellow:
                    return True
        return False

    def check(self, choice):
        """
        Checks if the game has ended by  success
        :return: True if won or false if it has not ended yet
        """
        if self.check_column(choice) or self.check_line(choice) or self.check_diag1(choice) or self.check_diag2(choice):
            return True
        return False

    def check_future(self, color, choice):
        """
        Check but in advance
        :param choice: tuple
        param type_Strng: yellow or red
        :return: True or False
        """
        x = choice[0]
        y = choice[1]
        if color == -1:
            self.make_move('red', x, y)
        elif color == 1:
            self.make_move('yellow', x, y)
        state = self.check(choice)
        self.undo_move(choice)
        if state:
            return True
        return False

    def undo_move(self, choice):
        """
        Undoes a move
        :param choice: the last move which needs to be undo-ed
        :return: True if succesful
        """
        x = choice[0]
        y = choice[1]
        if self._board[x][y].red:
            self._board[x][y].clear_red()
            return True
        else:
            self._board[x][y].clear_yellow()
            return True

    def moves(self):
        """
        Tests if a game is a draw after this move, returns True if so or the number of moves until
        here, undoes the move
        :return: True if draw or the number of moves
        """
        contor = 0
        for line in self._board:
            for el in line:
                if not el.empty:
                    contor += 1
        if contor == 42:
            return True
        return contor


class GameError (Exception):

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message
