import unittest
import ChessEngine as ce
import chess as ch

class TestEvaluationFunction(unittest.TestCase):

    def test_start_board_eval_function(self):
        test_engine = ce.Engine(ch.Board(ch.STARTING_BOARD_FEN), 3)
        self.assertEqual(test_engine.evaluate(), 0)
    def test_one_white_pawn_eval(self):
        test_engine = ce.Engine(ch.Board('8/8/8/8/8/3P4/8/8'), 3)
        self.assertEqual(test_engine.evaluate(), 1)
    def test_one_white_pawn_eval_with_rook(self):
        test_engine = ce.Engine(ch.Board('8/3r4/8/8/8/3P4/8/8'), 3)
        self.assertEqual(test_engine.evaluate(), -4)

class TestAlphaBetaPruning(unittest.TestCase):

    def test_start_board_eval_function(self):
        test_engine = ce.Engine(ch.Board('1k6/2p1p3/8/8/8/8/4R3/1K6'), 2)
        score = test_engine.minimax(1, True)
        self.assertEqual(score, 4)
        print(test_engine.CandidateMove)




if __name__ == '__main__':
    unittest.main()