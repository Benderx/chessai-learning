import Engine
import math
import random
import os

class Player():
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def get_color(self):
        return(self.color)

    def last_move(self):
        return((self.lastX,self.lastY))

    def update_last(self, x, y):
        self.lastX = x
        self.lastY = y

    def get_type(self):
        raise Exception('not implemented')


class AiRand(Player):
    def __init__(self, color, engine):
        super().__init__(color, engine)

    def get_move(self, moves):
        return(random.choice(moves))

    def get_type(self): #could just inherit with self.type
        return('Random AI')


class AiMinimax(Player):
    def __init__(self, color, engine):
        super().__init__(color, engine)

    def get_move(self, moves):
        #return(random.choice(moves))
        m_arr = moves
        moves_arr = []
        for x in m_arr:
            self.engine.push_move(x)
            value = self.minimax(1, math.inf * -1, math.inf, self.color * -1)
            #if value != 0:
                #print ("move " + str(x) + " eval " + str(value))
            self.engine.pop_move()
            moves_arr.append((value, x)) #normalize so both colors look for largest val
        #print("moves: ")
        #for x in moves_arr:
        #    print(x)
        best_move = moves_arr[0]
        b_arr = [best_move]
        if self.color == 1: #white, look for most positive value
            for x in moves_arr:
                if x[0] > best_move[0]:
                    b_arr = [x]
                    best_move = x
                elif x[0] == best_move[0]:
                    b_arr.append(x)
        else: #black, look for most negative value
            for x in moves_arr:
                if x[0] < best_move[0]:
                    b_arr = [x]
                    best_move = x
                elif x[0] == best_move[0]:
                    b_arr.append(x)
            
        best_move = random.choice(b_arr)
        if len(b_arr) < 10:
            print ("best moves " + str(b_arr))
        print (best_move[0])
        return best_move[1]

    def get_type(self): #could just inherit with self.type
        return('Minimax AI')

    def evaluate(self, color, depth): #Returns a score for the current board state
        score = 0.0

        own_moves = self.engine.get_legal_moves(color)
        enemy_moves = self.engine.get_legal_moves(color * -1)

        own_pieces = []
        enemy_pieces = []

        w = self.engine.is_terminal(color, own_moves) #check if current color lost 
        if w != None:
            if w == 0:
                score = 0
                return score
            else:
                score = (1000 + depth)  * w  #return math.inf on white win, -inf on black win
                return score
        check = self.engine.in_check(color)
        if check:
            if len(own_moves) == 0:
                return (1000 + depth) * -1 * color
            else:
                score += 0.51 * color * -1
        if len(own_moves) == 0: #stalemate
            print("saw stalemate")
            return 0.0



        board = self.engine.get_board()
        for row in range(8):
            for col in range(8):
                square = board[col][row]
                if square != None:
                    if square.get_piece() == "Pawn":
                        if square.get_color() == color:
                            own_pieces.append(("Pawn", (row,col)))
                        else:
                            enemy_pieces.append(("Pawn", (row,col)))
                        score += 1 * square.get_color()
                    elif square.get_piece() == "Night":
                        if square.get_color() == color:
                            own_pieces.append(("Night", (row,col)))
                        else:
                            enemy_pieces.append(("Night", (row,col)))
                        score += 3 * square.get_color()
                    elif square.get_piece() == "Bishop":
                        if square.get_color() == color:
                            own_pieces.append(("Bishop", (row,col)))
                        else:
                            enemy_pieces.append(("Bishop", (row,col)))
                        score += 3 * square.get_color()
                    elif square.get_piece() == "Rook":
                        if square.get_color() == color:
                            own_pieces.append(("Rook", (row,col)))
                        else:
                            enemy_pieces.append(("Rook", (row,col)))
                        score += 4 * square.get_color()
                    elif square.get_piece() == "Queen":
                        if square.get_color() == color:
                            own_pieces.append(("Queen", (row,col)))
                        else:
                            enemy_pieces.append(("Queen", (row,col)))
                        score += 9 * square.get_color()
                    elif square.get_piece() == "King":
                        if square.get_color() == color:
                            #own_pieces.append(("King", (row,col)))
                            own_king_pos = (row,col)
                        else:
                            #enemy_pieces.append(("King", (row,col)))
                            enemy_king_pos = (row,col)
        if len(own_pieces) <= 1 and len(own_pieces) != 0:
            score += -0.01 * self.get_distance(own_king_pos, enemy_king_pos) * color * -1
            if enemy_king_pos[0] == 0 or enemy_king_pos[1] == 0:
                score += .05 * color
            #when few pieces remain, incentivize king to get involved

        if color == 1:
            score += .1 * (len(own_moves) - len(enemy_moves))
        else: #always calculate white moves - black moves
            score += .1 * (len(enemy_moves) - len(own_moves))
        #print (own_pieces)
        return score

    def minimax(self, depth, alpha, beta, color):
        val = self.evaluate(color, depth)
        #print (val)

        if depth == 0 or val > 900 or val < -900:            
            return val
        
        move_list = self.engine.get_legal_moves(color)

        if color == 1: #white
            v = -1 * math.inf
            for x in move_list:
                self.engine.push_move(x)
                v = max(v, self.minimax(depth - 1, alpha, beta, -1))
                self.engine.pop_move()  
                if beta <= alpha:
                    print("beta cutoff")
                    break 
            return v
            
        else: #black
            v = math.inf 
            for x in move_list:
                self.engine.push_move(x)
                v = min(v, self.minimax(depth - 1, alpha, beta, 1))
                self.engine.pop_move()
                beta = min(beta, v)
                if beta <= alpha:
                    print("alpha cutoff")
                    break
            return v

    def get_distance(self, a, b): #takes in 2 tuples, (x1,y1), (x2,y2)
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1]) **2)


class Human(Player):
    def __init__(self, color, engine, renderer):
        super().__init__(color, engine)
        #self.renderer = renderer

    def get_move(self, moves):
        #move = input("move? Format ((x,y),(x,y), None, 'normal')")
        #return move
        raise Exception('get_move for player is not implemented')
        # win = self.renderer.get_window()
        # maxWidth = self.renderer.get_width()

        # board = self.engine.get_board()

        # while True:
        #     alley = (win.getMouse()).getX()
        #     choice = int(alley // (maxWidth / 7))

        #     if choice in moves:
        #         return(choice)
        #     print('pick a real move')

    def get_type(self):
        return('Human')


class AiMonte(Player):
    def __init__(self, color, engine, samples):
        super().__init__(color, engine)
        self.samples = samples

    def get_move(self, moves):
        children = len(moves)
        children_vals = children*[0]
        curr_samples = self.samples
        samples_per_child = curr_samples//children

        #THINK HARDER
        while samples_per_child == 0:
            curr_samples += 1
            samples_per_child = curr_samples//children
        print(samples_per_child, 'per child. total children:', children)

        child_index = 0
        for child in moves:
            for i in range(samples_per_child):
                self.engine.push_move(child)
                
                inv_color = self.engine.invert_color(self.color)
                winner = self.hard_rollout(inv_color)
                self.engine.pop_move()

                if winner == self.color:
                    children_vals[child_index] += 1
                elif winner == inv_color:
                    children_vals[child_index] -= 1
            child_index += 1


        best_path = max(children_vals)
        a = children_vals.index(best_path)
        return(moves[a])

    def hard_rollout(self, color):
        moves = self.engine.get_legal_moves(color)
        node_state  = self.engine.is_terminal(color, moves)

        if node_state != None:
            return(node_state)
        else:
            inv_color = self.engine.invert_color(color)

            next_move = random.choice(moves)
            self.engine.push_move(next_move)
            v = self.hard_rollout(inv_color)
            self.engine.pop_move()
            return(v)

    def get_type(self):
        return('Monte Carlo AI')
