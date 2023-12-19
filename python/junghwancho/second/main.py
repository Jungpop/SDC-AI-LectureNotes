import socket
from time import sleep

from server_socket.service.ServerSocketServiceImpl import ServerSocketServiceImpl

if __name__ == '__main__':
    serverSocketService = ServerSocketServiceImpl()
    serverSocketService.createServerSocket("0.0.0.0", 33333)
    serverSocketService.setSocketOption(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    serverSocketService.bindServerSocket()
    serverSocketService.setServerListenNumber(15)
    serverSocketService.setBlockingOperation()

    while True:
        try:
            serverSocketService.acceptClientSocket()

        except socket.error:
            sleep(0.5)
