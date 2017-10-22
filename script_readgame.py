import Engine
import Player
import BoardConverter

decoder = BoardConverter.BoardDecoder()
for move in decoder.read_game(0):
	print("Move is:", move[71])
	print(move)
	print('\n')
# decoder.read_all()