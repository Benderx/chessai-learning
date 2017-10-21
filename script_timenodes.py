import Engine
import Player
import time

# def play_game():
#     engine = Engine.Engine()
#     engine.init_board()

#     PLAYER_ONE = Player.AiRand(1, engine)
#     PLAYER_TWO = Player.AiRand(-1, engine)

#     players = [PLAYER_ONE,PLAYER_TWO]

#     turn = 0

#     i_time = time.clock()
#     while True:
#         possible_moves = engine.get_legal_moves(players[turn].get_color())
#         winner = engine.is_terminal(players[turn].get_color(), possible_moves)
#         if winner != None:
#             break

#         move = players[turn].get_move(possible_moves)
#         engine.perform_move(move)

#         turn = 1-turn
#     e_time = time.clock()
#     return (e_time - i_time) / float(engine.get_game_length())


# total = 0
# total_i = 0
# for i in range(100):
#     total += play_game()
#     total_i += 1
# print('Nodes per second over {0} games: {1}'.format(total_i, 1.0/(total/total_i)))



def get_time():
    engine = Engine.Engine()
    engine.init_board()

    PLAYER_ONE = Player.AiRand(1, engine)
    PLAYER_TWO = Player.AiRand(-1, engine)

    players = [PLAYER_ONE,PLAYER_TWO]

    turn = 0
    num = 10000

    while True:

        i_time = time.clock()
        for j in range(num):
            if True:
                possible_moves = engine.get_legal_moves(players[turn].get_color(), True)
                exit()
            else:
                possible_moves = engine.get_legal_moves(players[turn].get_color())
        e_time = time.clock()

        calc1 = (e_time-i_time)/float(num)
        print('time taken on get_legal_moves over {0} iterations on turn {1}: {2:.{3}e}'.format(num, engine.get_game_length(), calc1, 4))
        


        i_time = time.clock()
        for j in range(num):
            winner = engine.is_terminal(players[turn].get_color(), possible_moves)
        e_time = time.clock()

        calc2 = (e_time-i_time)/float(num)
        print('time taken on is_terminal over {0} iterations on turn {1}: {2:.{3}e}'.format(num, engine.get_game_length(), calc2, 4))



        if winner != None:
            break


        i_time = time.clock()
        for j in range(num):
            move = players[turn].get_move(possible_moves)
        e_time = time.clock()

        calc3 = (e_time-i_time)/float(num)
        print('time taken on get_move over {0} iterations on turn {1}: {2:.{3}e}'.format(num, engine.get_game_length(), calc3, 4))

        print()

        engine.perform_move(move)

        turn = 1-turn


t = get_time()
