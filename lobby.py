from identification import go_online, go_offline, set_username
from find_users import find_online_users
from game import game_server, game_client


print('LOGIC FOR GETTING USERNAME')
username = 'PLACEHOLDER'
set_username(username)

  # sample menu program
while True:

  # print online users
  print('online users:')
  print('SOME LOGIC FOR PRINTING ONLINE USERNAMES')

  # get input
  user_input = input('--MENU--\n(1) Go Online (wait for incoming connections)\n(2) Play against an Online Player\n(3)Refresh\n-->')
  while user_input != '1' and user_input != '2' and user_input != '3':
    print('WRITE AN ERROR MESAGE AND REPROMPT')

  if user_input == '1':
    go_online()
    game_server()
    go_offline()
  
  elif user_input == '2':
    print('LOGIC FOR PRINTING ONLINE USERS LIST')
    print('LOGIC FOR ASKING USERNAME WHO THEY WANT TO PLAY AGAINST')
    print('LOGIC FOR VERIFYING THE INPUT OF THE USER')
    print('LOGIC FOR GETTING THE IP ADDRESS OF THE USERNAME FROM ONLINE USERS LIST')
    chosen_opponent = '0.0.0.0' # set this according to user's input
    game_client(chosen_opponent)

  elif user_input == '3':
      # next iteration will print the new online users
    continue