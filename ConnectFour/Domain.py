

class Square:
    """ This class represents a dot in the board of the game. """
    c=0
    def __init__(self):
        self._ID = Square.c
        Square.c += 1
        self._empty = True
        self._red = False
        self._yellow = False

    def __str__(self):
        s = ''
        if self.empty:
            s += u' '
        elif self.red:
            s += u'○'
        elif self.yellow:
            s += u'●'
        else:
            s = s
        return s

    def __eq__(self, other):
        if self._ID == other.ID and self.empty == other.empty:
            return True
        return False

    @property
    def empty(self):
        """ is_empty getter """
        return self._empty

    @empty.setter
    def empty(self, new_value):
        """ is_empty setter, sets it to False """
        self._empty = new_value

    @property
    def red(self):
        """ Red getter. Checks if square is red """
        return self._red

    @property
    def yellow(self):
        """ Yellow getter. Checks if square is yellow """
        return self._yellow

    @red.setter
    def red(self, new_value):
        """ Makes a move and fills a dot with red """
        if self.empty is True and self.yellow is False and self.red is False and new_value is True:
            self._red = new_value
            self.empty = False
        else:
            raise DomainError('Square already full! ')

    @yellow.setter
    def yellow(self, new_value):
        """ Makes a move and fills a dot with yellow """
        if self.empty is True and self.yellow is False and self.red is False and new_value is True:
            self._yellow = new_value
            self.empty = False
        else:
            raise DomainError('Square already full! ')

    def clear_red(self):
        """
        Used for undo.. clears red
        :return: the value of new red
        """
        self._red = False
        self.empty = True
        return self.red

    def clear_yellow(self):
        """
        Used for undo.. clears yellow
        :return: the new value of yelow
        """
        self._yellow = False
        self.empty = True
        return self.yellow


class DomainError(Exception):

    """ Class for Domain errors """
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message
