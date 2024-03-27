import chess as ch

#Starting position: board = ch.STARTING_BOARD_FEN

class Engine:
    def __init__(self, board, depth):
        self.board = board
        # self.FEN = self.board.board_fen()
        #chess.Board, not chess.BaseBoard
        self.depth = depth
        self.CandidateMove = None
    
    #AlphaBeta Algorithmn
        
    # def alphaBetaMax(self, alpha : float, beta : float , depth : int):

    #     #Base Case
    #     if depth == 0 or self.board2.legal_moves.count() == 0:
    #         return self.evaluate()
    #     for move in self.board2.legal_moves:
    #         self.board2.push(move)
    #         print(self.board2.fen())
    #         temp_alpha = self.alphaBetaMin(alpha, beta, depth-1)
    #         if temp_alpha >= beta:
    #             return beta
    #         if temp_alpha > alpha:
    #             alpha = temp_alpha
    #         self.board2.pop()
    #     return alpha
        
    
    # def alphaBetaMin(self, alpha : float, beta : float, depth : int):
    #     # Base Case
    #     if depth == 0 or self.board2.legal_moves.count() == 0:
    #         return self.evaluate()
    #     for move in self.board2.legal_moves:
    #         self.board2.push(move)
    #         temp_beta = self.alphaBetaMin(alpha, beta, depth-1)
    #         if temp_beta <= alpha:
    #             return alpha
    #         if temp_beta < beta:
    #             beta = temp_beta
    #         self.board2.pop()
    #     return beta
        

    def minimax(self, depth, maxPlayer):
        if depth == 0 or self.board.legal_moves.count() == 0:
            return self.evaluate()
        if maxPlayer:
            maxEval = float('-inf')
            # for move in self.board2.legal_moves:
            #     print(f"LEGAL MOVE: {move} ", end = " ")
            for move in self.board.legal_moves:
                   self.board.push(move)
                   eval = self.minimax(depth-1, False) 
                   self.board.pop()
                   maxEval = max(eval, maxEval)
                   if(maxEval == eval):
                        self.CandidateMove = move
            return maxEval
        else:
            minEval = float('inf')
            for move in self.board.legal_moves:
                   self.board.push(move)
                   eval = self.minimax(depth-1, True) 
                   self.board.pop()
                   minEval = min(eval, minEval)
            return minEval            
    

    
    #Returns the evaluation function
    def evaluate(self) -> float:
        white_sum = 0
        black_sum = 0
        for i in range(64):
            if(self.board.color_at(ch.SQUARES[i]) == ch.WHITE):
                white_sum += self.single_piece_eval(ch.SQUARES[i])
            else:
                black_sum += self.single_piece_eval(ch.SQUARES[i])
        return white_sum - black_sum

    #Gets the evaluation of a single piece
    def single_piece_eval(self, square):
        if(self.board.piece_type_at(square) == ch.PAWN):
            return 1
        elif(self.board.piece_type_at(square) == ch.KNIGHT):
            return 3
        elif(self.board.piece_type_at(square) == ch.BISHOP):
            return 3
        elif(self.board.piece_type_at(square) == ch.ROOK):
            return 5
        elif(self.board.piece_type_at(square) == ch.QUEEN):
            return 8    
        return 0 
    

# UCI PROTOCOL 
    
while True:
    args = input().split()
    if args[:2] == ["position", "startpos"]:
        pass
    elif args[0] == "go":
        cur_engine = Engine(ch.Board(ch.STARTING_BOARD_FEN), 1)
        cur_engine.minimax(2, True)
        move = cur_engine.CandidateMove
        print("bestmove", move)
