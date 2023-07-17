# installation:

```
git clone https://github.com/hesam-zahiri/Safe_Chat.git
```
# How to use:
```
cd Safe_Chat
```
```
python3 safe-chat.py
```
- open the new tab (ctrl+shift+t)
- telnet (Your IP Address) (Your Port) (In Default mode, it is saved on localhost)
- and type this command:
```
telnet (ip Address) (Port Address) / telnet 127.0.0.1 55555
```
- enter your neme
- After entering your name, go back to the previous tab
- Now you can enjoy secure chat.
# How it works?
- The program first creates a TCP/IP socket and binds it to a local port. Then the program waits for a client to connect to the port. When a client connects, the program creates a new thread and delegates it to handle(). handle() is responsible for managing the client. The client can send any message it wants and handle() will send that message to all other clients. When a client is disconnected, handle() removes that client from the list of clients and sends a message to all other clients indicating that the client has left the chat room.
To run this program, run it in a terminal. Then a client can connect to the chat room by connecting to the port. The client can send any message it wants and that message will be sent to all other clients.
- So feel free to chat and enjoy security‼️



