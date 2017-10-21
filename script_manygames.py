import Engine
import Player
import time

ww = 0
bw = 0
d = 0

games = 1000

while games > 0:
    winner = None
    engine = Engine.Engine()
    engine.init_board()

    PLAYER_ONE = Player.AiRand(1,engine)
    PLAYER_TWO = Player.AiMonte(-1,engine, 1000)

    players = [PLAYER_ONE,PLAYER_TWO]

    turn = 0

    while True:
        possible_moves = engine.get_legal_moves(players[turn].get_color())
        winner = engine.is_terminal(players[turn].get_color(), possible_moves)
        if winner != None:
            if winner == 1:
                print("Results are in: White wins")
                ww+=1
            elif winner == -1:
                print("Results are in: Black wins")
                bw+=1
            else:
                print("Results are in: Draw")
                d +=1
            break
        move = players[turn].get_move(possible_moves)
        engine.perform_move(move)
        print('move')
        turn = 1-turn
    games-=1
print("White won:",ww)
print("Black won:",bw)
print("There were draws:",d)