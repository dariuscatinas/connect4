import unittest
from GameSimulation import *
from AI import AI,Node


class TestGame(unittest.TestCase):

    def setUp(self):

        self.game = GameSimulation()
        self.ai = AI(self.game)

    def tearDown(self):
        #print(str(self.game))
        pass

    def test_available(self):

        self.assertEqual(len(self.game.available()), 7)
        self.assertEqual(self.game.available()[0], (5, 0))
        self.assertEqual(self.game.available()[6], (5, 6))
        self.assertTrue(self.game.make_move('yellow', 5, 0))
        self.assertEqual(self.game.available()[0], (4, 0))
        self.assertEqual(self.game.available()[1], (5, 1))
        self.assertTrue(self.game.make_move('red', 4, 0))
        self.assertTrue(self.game.make_move('red', 3, 0))
        self.game.make_move('red', 2, 0)
        self.game.make_move('red', 1, 0)
        self.assertEqual(self.game.available()[0], (0, 0))
        self.game.make_move('red', 0, 0)
        self.assertEqual(len(self.game.available()), 6)
        self.assertRaises(Exception, self.game.make_move, 'red', 0, 0)
        self.assertRaises(Exception, self.game.make_move, 'yellow', 2, 0)

    def test_win_diag1_1(self):

        self.assertTrue(self.game.make_move('red', 5, 0))
        self.assertTrue(self.game.make_move('yellow', 5, 1))
        self.assertTrue(self.game.make_move('yellow', 5, 2))
        self.assertTrue(self.game.make_move('yellow', 5, 3))
        self.assertTrue(self.game.make_move('red', 4, 1))
        self.assertFalse(self.game.check_diag1((4, 1)))
        self.assertTrue(self.game.make_move('yellow', 4, 2))
        self.assertTrue(self.game.make_move('yellow', 4, 3))
        self.assertTrue(self.game.make_move('yellow', 3, 3))
        self.assertTrue(self.game.make_move('red', 3, 2))
        self.assertTrue(self.game.make_move('red', 2, 3))
        self.assertTrue(self.game.check_diag1((2, 3)))

    def test_win_diag1_2(self):

        self.assertTrue(self.game.make_move('yellow', 5, 2))
        self.assertTrue(self.game.make_move('yellow', 5, 3))
        self.assertTrue(self.game.make_move('red', 5, 4))
        self.assertTrue(self.game.make_move('yellow', 5, 5))
        self.assertTrue(self.game.make_move('red', 4, 2))
        self.assertTrue(self.game.make_move('red', 3, 2))
        self.assertTrue(self.game.make_move('yellow', 4, 3))
        self.assertTrue(self.game.make_move('red', 3, 3))
        self.assertTrue(self.game.make_move('red', 2, 3))
        self.assertTrue(self.game.make_move('yellow', 4, 4))
        self.assertTrue(self.game.make_move('yellow', 3, 4))
        self.assertTrue(self.game.make_move('red', 2, 4))
        self.assertTrue(self.game.make_move('yellow', 4, 5))
        self.assertTrue(self.game.make_move('yellow', 3, 5))
        self.assertTrue(self.game.make_move('red', 2, 5))
        self.assertTrue(self.game.make_move('yellow', 1, 5))
        self.assertTrue(self.game.make_move('red', 0, 5))
        self.assertTrue(self.game.make_move('red', 1, 4))
        self.assertTrue(self.game.check_diag1((1, 4)))
        self.assertFalse(self.game.check_diag2((1, 4)))

    def test_win_diag2_1(self):

        self.assertTrue(self.game.make_move('yellow', 5, 1))
        self.assertTrue(self.game.make_move('yellow', 4, 1))
        self.assertTrue(self.game.make_move('yellow', 3, 1))
        self.assertTrue(self.game.make_move('yellow', 5, 2))
        self.assertFalse(self.game.check_diag1((5, 2)))
        self.assertTrue(self.game.make_move('yellow', 4, 2))
        self.assertTrue(self.game.make_move('red', 3, 2))
        self.assertFalse(self.game.check_diag2((3, 2)))
        self.assertTrue(self.game.make_move('yellow', 5, 3))
        self.assertTrue(self.game.make_move('red', 4, 3))
        self.assertTrue(self.game.make_move('red', 5, 4))
        self.assertTrue(self.game.make_move('red', 2, 1))
        self.assertTrue(self.game.check_diag2((2, 1)))
        self.assertTrue(self.game.check((2, 1)))

    def test_win_line(self):

        self.assertTrue(self.game.make_move('red', 5, 0))
        self.assertTrue(self.game.make_move('red', 5, 1))
        self.assertTrue(self.game.make_move('red', 5, 2))
        self.assertTrue(self.game.make_move('red', 5, 3))
        self.assertTrue(self.game.make_move('red', 5, 4))
        self.assertTrue(self.game.check_line((5, 6)))

    def test_win_column(self):

        self.assertTrue(self.game.make_move('red', 5, 0))
        self.assertTrue(self.game.make_move('red', 4, 0))
        self.assertTrue(self.game.make_move('red', 3, 0))
        self.assertTrue(self.game.make_move('red', 2, 0))
        self.assertTrue(self.game.check_column((1, 0)))
        self.assertTrue(self.game.check((1, 0)))

    def test_ai(self):
        self.assertTrue(self.game.make_move('red', 5, 0))
        self.assertTrue(self.game.make_move('yellow', 5, 1))
        self.assertTrue(self.game.make_move('red', 5, 2))
        self.assertTrue(self.game.make_move('red', 5, 3))
        self.assertTrue(self.game.make_move('yellow', 5, 4))
        self.assertTrue(self.game.make_move('red', 5, 5))
        self.assertTrue(self.game.make_move('red', 5, 6))
        self.assertTrue(self.game.make_move('yellow', 4, 1))
        self.assertTrue(self.game.make_move('yellow', 4, 2))
        self.assertTrue(self.game.make_move('red', 4, 3))
        self.assertTrue(self.game.make_move('yellow', 4, 4))
        self.assertTrue(self.game.make_move('yellow', 4, 5))
        self.assertTrue(self.game.make_move('yellow', 4, 6))
        self.assertTrue(self.game.make_move('red', 3, 1))
        self.assertTrue(self.game.make_move('red', 3, 3))
        self.assertTrue(self.game.make_move('yellow', 3, 2))
        self.assertTrue(self.game.make_move('red', 3, 4))
        self.assertTrue(self.game.make_move('red', 3, 5))
        self.assertTrue(self.game.make_move('yellow', 3, 6))
        self.assertTrue(self.game.make_move('yellow', 2, 2))
        self.assertTrue(self.game.make_move('yellow', 2, 3))
        self.assertTrue(self.game.make_move('red', 2, 4))
        self.assertTrue(self.game.make_move('yellow', 2, 5))
        self.assertTrue(self.game.make_move('red', 2, 6))
        self.assertTrue(self.game.make_move('yellow', 1, 5))

        self.ai.game = self.game
        self.assertEqual(self.ai.minimax(Node(self.game), 1000, -1000, -1, (1, 5)), 5)


if __name__ == '__main__':
    unittest.main()