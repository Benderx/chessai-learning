import random
import time
import connect_engine
import os

class Player():
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def get_color(self):
        return(self.color)

    def last_move(self):
        return((self.lastX,self.lastY))

    def update_last(self,x,y):
        self.lastX = x
        self.lastY = y

    def get_type(self):
        raise Exception('not implemented')


class AiRand(Player):
    def __init__(self,color, engine):
        super().__init__(color, engine)

    def get_move(self, moves):
        return(random.choice(moves))

    def get_type(self): #could just inherit with self.type
        return('Random AI')


class Human(Player):
    def __init__(self, color, engine, renderer):
        super().__init__(color, engine)
        self.renderer = renderer

    def get_move(self, moves):
        win = self.renderer.get_window()
        maxWidth = self.renderer.get_width()

        board = self.engine.get_board()

        while True:
            alley = (win.getMouse()).getX()
            choice = int(alley // (maxWidth / 7))

            if choice in moves:
                return(choice)
            print('pick a real move')

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

        # print('getting move with', samples_per_child)

        child_index=0

        for child in moves:
            for i in range(samples_per_child):
                self.engine.push_move(child, self.color)
                
                inv_color = self.engine.invert_color(self.color)
                winner = self.hard_rollout(inv_color)
                self.engine.pop_move()

                if winner == self.color:
                    children_vals[child_index]+=1
                elif winner == inv_color:
                    children_vals[child_index]-=1
            child_index+=1


        best_path = max(children_vals)
        a = children_vals.index(best_path)
        return(moves[a])

    def hard_rollout(self,color):
        moves = self.engine.get_legal_moves()
        node_state  = self.engine.is_terminal(color,moves)

        if node_state != 0:
            return(node_state)
        else:
            inv_color = self.engine.invert_color(color)

            next_move = random.choice(moves)
            self.engine.push_move(next_move,color)
            v = self.hard_rollout(inv_color)
            self.engine.pop_move()
            return(v)

    def get_type(self):
        return('Monte Carlo AI')
