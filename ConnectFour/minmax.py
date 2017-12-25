class Node:

    def __init__(self, board, move):

        self._value = None
        self._depth = None
        self._board = board
        self.move = move

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, new_value):
        self._depth = new_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,new_value):
        self.value = new_value

    pass