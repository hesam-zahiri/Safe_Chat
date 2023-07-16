import socket
import threading

class ChatRoom:
    def __init__(self):
        self.host = '127.0.0.1'  # Local IP address
        self.port = 55555  # Port to connect

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the chat!'.encode('ascii'))
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'Connected with {str(address)}')

            client.send('name:'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}!')
            self.broadcast(f'{nickname} joined the chat!'.encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            client.send('You are now connected!Now go back to the previous page.'.encode('ascii'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def start(self):
        print('Server started! open the new page and type: Open a new tab and follow the instructions.(ctrl+shift+T)')
        self.receive()


if __name__ == '__main__':
    chat_room = ChatRoom()
    chat_room.start()

