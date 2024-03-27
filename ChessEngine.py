import chess as ch

#Starting position: board = ch.STARTING_BOARD_FEN

class Engine:
    def __init__(self, board, depth):
        self.board = board
        self.depth = depth
        self.CandidateMove = None
    
    #AlphaBeta Algorithmn
        
    def alphaBetaMax(self, alpha : float, beta : float , depth : int):

        #Base Case
        if depth == 0 or self.board.legal_moves.count() == 0:
            self.CandidateMove = move
            return self.evaluate()
        for move in self.board.legal_moves():
            self.board.push(move)
            #Temp alpha
            temp_alpha = self.alphaBetaMin(alpha, beta, depth-1)
            self.board.pop()
            if temp_alpha >= beta:
                self.CandidateMove = move
                return beta
            if temp_alpha > alpha:
                alpha = temp_alpha
        self.CandidateMove = move
        return alpha
        
    
    def alphaBetaMin(self, alpha : float, beta : float, depth : int):
        # Base Case
        if depth == 0 or self.board.legal_moves.count() == 0:
            self.CandidateMove = move
            return self.evaluate()
        for move in self.board.legal_moves():
            self.board.push(move)
            temp_beta = self.alphaBetaMin(alpha, beta, depth-1)
            if temp_beta <= alpha:
                self.CandidateMove = move
                return alpha
            if temp_beta < beta:
                beta = temp_beta
        self.CandidateMove = move
        return beta

    
    #Returns the evaluation function. If position is true, return white's pov
    def evaluate(self) -> float:
        white_sum = 0
        black_sum = 0
        for i in range(64):
            if(self.board.color_at(ch.SQUARES[i]) == ch.WHITE):
                white_sum += self.single_piece_eval(ch.SQUARES[i])
            else:
                black_sum += self.single_piece_eval(ch.SQUARES[i])
        return white_sum - black_sum



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
    
