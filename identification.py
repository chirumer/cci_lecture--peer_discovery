import socket
import time
import errno
import threading

IDENTIFICATION_PORT = 5005
# clients broadcast to this port to identify users on the network

class Controller_token:
  def __init__(self):
    self.is_active = False
  def enable(self):
    self.is_active = True
  def disable(self):
    self.is_active = False
# for controlling identification

# identification thread's job
def start_identification(identification_controller):
  identification_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  server_address = ''
  identification_endpoint = (server_address, IDENTIFICATION_PORT)
  identification_socket.bind(identification_endpoint)

  identification_socket.setblocking(False)

  while True:

    while not identification_controller.is_active:
      time.sleep(0.1)

    try:
      max_data_size = 1000
      payload, client_endpoint = identification_socket.recvfrom(max_data_size)

    except socket.error as e:
      if e.errno == errno.EAGAIN:
        time.sleep(0.1)
        continue

    command = payload.decode()
    if command == 'identify':
        # they are querying our username
      username = 'CCI'
      encoded_username = username.encode()
      identification_socket.sendto(encoded_username, client_endpoint)
      # we send our username

identification_controller = Controller_token()
identification_thread = threading.Thread(target=start_identification, args=(identification_controller,))
identification_thread.start()

identification_controller.enable()
print('identification enabled')
# start identification

# time.sleep(1)

# identification_controller.disable()
# print('identification disabled')
# # stop identification

# time.sleep(1)

# identification_controller.enable()
# print('identification enabled')
# # start identification

# time.sleep(1)

# identification_controller.disable()
# print('identification disabled')
# # stop identification
