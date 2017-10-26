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
        print (self.color)

    def get_move(self, moves):
        #return(random.choice(moves))
        m_arr = moves
        moves_arr = []
        #print("m_arr: " + str(m_arr))
        for x in m_arr:
            #print("testing move " + str(x))
            self.engine.push_move(x)
            #print(self.move_stack)
            #print('')
            #self.engine.print_board()
            value = self.minimax(2, self.color * -1, math.inf * -1, math.inf)
            if value != 0:
                print ("move " + str(x) + " eval " + str(value))
            #print(self.move_stack)
            self.engine.pop_move()
            moves_arr.append((self.color * value, x))
        #print ("moves_arr: " + str(moves_arr))
        best_move = moves_arr[0]
        b_arr = [best_move]
        for x in moves_arr:
            #print("x = "+str(x))
            #print("best_move = " + str(best_move))
            if x[0] > best_move[0]:
                #print("x is better")
                b_arr = [x]
                best_move = x
            elif x[0] == best_move[0]:
                b_arr.append(x)
            #print("best_move = " + str(best_move))
        #print(moves_arr)
        #print(b_arr)
        
        best_move = random.choice(b_arr)
        if len(b_arr) < 10:
            print ("best moves " + str(b_arr))
        return best_move[1]

    def get_type(self): #could just inherit with self.type
        return('Minimax AI')

    def evaluate(self, color): #Returns a score for the current board state
        score = 0.0
        w = self.engine.is_terminal(color,self.engine.get_legal_moves(color)) #check if current color lost 
        if w != None:
            if w == 0:
                score = 0
                return score
            else:
                score = math.inf * w #return math.inf on white win, -inf on black win
                return score
        if self.engine.in_check(-1*color):
            score += 0.51
            print("CHECK")
            self.engine.print_board()

        board = self.engine.get_board()
        for row in board:
            for square in row:
                if square != None:
                    if square.get_piece() == "Pawn":
                        score += 1 * square.get_color()
                    elif square.get_piece() == "Night":
                        score += 3 * square.get_color()
                    elif square.get_piece() == "Bishop":
                        score += 3 * square.get_color()
                    elif square.get_piece() == "Rook":
                        score += 4 * square.get_color()
                    elif square.get_piece() == "Queen":
                        score += 9 * square.get_color()
        return score

    def minimax(self, depth, color, minimum, imum):
        val = self.evaluate(color)

        if depth == 0 or val == math.inf or val == (-1 * math.inf):            
            return val
        
        if color == self.color:
            a = self.engine.get_legal_moves(color)
            v = minimum
            for x in a:
                #print ("testing move ", x)
                self.engine.push_move(x)
                v1 = self.minimax(depth - 1, -1 * self.color, v, maximum)
                self.engine.pop_move()  
                if v1 > v:
                    v = v1
                if v > maximum:
                    return maximum
            return v
            
        else: #not computer's turn
            b = self.engine.get_legal_moves(color)
            w = maximum 
            for x in b:
                self.engine.push_move(x)
                w1 = self.minimax(depth - 1, self.color, minimum, w)
                self.engine.pop_move()
                if w1 < w:
                    w = w1
                if w < minimum:
                    return minimum
            return w

class Human(Player):
    def __init__(self, color, engine, renderer):
        super().__init__(color, engine)
        self.renderer = renderer

    def get_move(self, moves):
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
