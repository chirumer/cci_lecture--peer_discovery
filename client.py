import socket


HOST = '127.0.0.1'
PORT = 558


# represents the game state
board = ''

def print_current_board():
  print('board:..')

def get_users_move():
  move = input('What is your move: ')
  return move

def update_game_state(player, move):
  global board
  # update the board
  board = board + move

  print(player + ' played ' + move)

def has_game_ended():
  if (board == 'abcd'):
    return True
  else:
    return False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as game_socket:
    game_socket.connect((HOST, PORT))
    print('Game Started')

    while True:

      print_current_board()
      move = get_users_move()
      update_game_state('user', move)
      game_socket.send(move.encode())
      if has_game_ended():
        break

      print("waiting for opp's move")
      opp_move = game_socket.recv(1024).decode()
      if not opp_move:
        break
      update_game_state('opp', opp_move)
      if has_game_ended():
        break

print_current_board()
print('Game ended')
