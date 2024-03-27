import unittest
import ChessEngine as ce
import chess as ch

class TestEvaluationFunction(unittest.TestCase):

    def test_start_board_eval_function(self):
        test_engine = ce.Engine(ch.BaseBoard(ch.STARTING_BOARD_FEN), 3)
        self.assertEqual(test_engine.evaluate(), 0)
    def test_one_white_pawn_eval(self):
        test_engine = ce.Engine(ch.BaseBoard('8/8/8/8/8/3P4/8/8'), 3)
        self.assertEqual(test_engine.evaluate(), 1)
    def test_one_white_pawn_eval_with_rook(self):
        test_engine = ce.Engine(ch.BaseBoard('8/3r4/8/8/8/3P4/8/8'), 3)
        self.assertEqual(test_engine.evaluate(), -4)



if __name__ == '__main__':
    unittest.main()