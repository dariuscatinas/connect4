from GameSimulation import *
from copy import deepcopy

class AI:

    def __init__(self, game):
        """

        :param game_simulation: a game simulation
        """
        self._game = game

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        self._first = value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, new_game):
        self._game = new_game

    def minimax(self, node, alpha, beta, color = -1, last_move = (3, 3)):
        '''
        A complicated algorithm... returns the next choice in an (x,y) tupple
        last_move is a tupple indicating the coordinates of the last move in a 0 indexed matrix
        node is the current node
        alpha represents the lower bound of the search
        beta represents the upper bound of the search
        color -> if 1 : yellow , if -1: red
        Modifies the state of the board
        :return: the best value
        '''
        # Recursively calculate the value of the next choice , it should be the max of the minimum of the other nodes.
        # This implementation is actually a negamax implementation due to the observation the value of the opposite
        # player is actually - the AI value, therefore there is no need of two algorithms
        if node.game.moves() == True: # trivial case, the board signals draw
            node.value = 0
            return node.value
        elif node.game.check(last_move): #the game is won
            if color == -1: # basically if the last move is won by the move of color -1 (red)(the color changes in the loop)
                node.value = 43 - node.game.moves()
            else:  # if the game is won by color 1 (yellow)
                node.value = - (43 - node.game.moves())
            return node.value                    # is going to be 42 -  the number of moves - > simple heuristic to order and get the best result

        max = (43 - node.game.moves()) // 2 # use maximum to get the next perfect choice
        if beta > max:
            beta = max # the  bound changes
            if alpha >= beta:
                return beta  # the case where the interval is just a number or it is shifted
        for tup in node.game.available():  # check for each possible state of the program
            if color == -1:
                new_game = deepcopy(node.game) # a new game is created
                new_game.make_move('red', tup[0], tup[1]) #it is modified
                color = - color
                value = - self.minimax(Node(new_game),alpha, beta, color,  tup) # that game( board state ) is passed to the new node
                if value >= beta:
                    return value
                if value > alpha:
                    alpha = value

            elif color == 1:
                new_game = deepcopy(node.game)
                new_game.make_move('yellow', tup[0], tup[1])
                color = - color
                value = self.minimax(Node(new_game),alpha, beta, color, tup)
                if value >= beta:
                    return value
                if value > alpha:
                    alpha = value
        return alpha


class Node:
    """
    Represents one node (state of the function)
    """
    def __init__(self, game):
        self._value = None
        self._game = game

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, new_game):
        self._game = new_game

