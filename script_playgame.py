import Engine
import Player

winner = None
engine = Engine.Engine()
engine.init_board()

PLAYER_ONE = Player.AiRand(1,engine)
PLAYER_TWO = Player.AiRand(-1,engine)

players = [PLAYER_ONE,PLAYER_TWO]

turn = 0

while not winner:
	possible_moves = engine.get_legal_moves(players[turn].get_color())
	winner = engine.is_terminal(players[turn].get_color(), possible_moves)
	print("\n\nBoardstate:")
	engine.print_board()
	print("Current players turn:", players[turn])
	print(possible_moves)
	move = players[turn].get_move(possible_moves)
	print("Move:", move)
	engine.update_board(move)
	turn = 1-turn