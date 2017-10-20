import Engine
import Player
import time

play_by_play = False

winner = None
engine = Engine.Engine()
engine.init_board()

PLAYER_ONE = Player.AiRand(1,engine)
PLAYER_TWO = Player.AiRand(-1,engine)

players = [PLAYER_ONE,PLAYER_TWO]

turn = 0

while True:
    possible_moves = engine.get_legal_moves(players[turn].get_color())
    winner = engine.is_terminal(players[turn].get_color(), possible_moves)
    print("\n\nBoardstate:")
    engine.print_board()
    print("Current players turn:", players[turn].get_color())
    print("All moves:\n",possible_moves)
    if winner:
        print("Results are in:",winner)
        break
    move = players[turn].get_move(possible_moves)
    print("Move:", move)
    engine.update_board(move)
    turn = 1-turn
    if play_by_play:
        input("")
    # time.sleep(1)