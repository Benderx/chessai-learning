import Engine
import Player
import time

play_by_play = True

winner = None
engine = Engine.Engine()
engine.init_board()

PLAYER_ONE = Player.AiRand(1, engine)
PLAYER_TWO = Player.AiMonte(-1, engine, 100)

players = [PLAYER_ONE,PLAYER_TWO]

turn = 0

print("Inital Boardstate:")
engine.print_board()

while True:
    possible_moves = engine.get_legal_moves(players[turn].get_color())
    winner = engine.is_terminal(players[turn].get_color(), possible_moves)
    print("Current players turn:", players[turn].get_color())
    # print("All moves:\n",possible_moves)
    if winner != None:
        if winner == 1:
            print("Results are in: White wins")
        elif winner == -1:
            print("Results are in: Black wins")
        else:
            print("Results are in: Draw")
        break
    move = players[turn].get_move(possible_moves)
    print("Move:", move)
    if move[0] != None:
        print('Piece moved:', engine.get_board()[move[0][1]][move[0][0]].get_piece())
    else:
        print('Piece moved:', 'castle or something')
    engine.perform_move(move)
    print("Boardstate:")
    engine.print_board()
    print('\n')

    turn = 1-turn
    print(engine.get_game_length())
    if play_by_play:
        input("")
    # time.sleep(1)
