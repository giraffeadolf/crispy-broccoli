import socketserver
from methods import TCPHandler

server = socketserver.TCPServer(("127.0.0.1", 7777), TCPHandler)

server.serve_forever()
