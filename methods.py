import socketserver
import socket
import json
import ssl
from db import session, user
from threading import Thread
from queue import Queue

socks = {}
names = []


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        data = self.request.recv(1024)
        data = data.decode()
        data = json.loads(data)
        q = Queue

        if data['action'] == 'msg':

            thrs = []

            q.put(data['message'])

            def send_msg(l):
                if q:
                    msg = q.get()
                    socks[l].send(msg)

            for login in socks:
                thrs.append(
                    Thread(target=send_msg, args=(login,))
                )

            for t in thrs:
                t.start()

            for t in thrs:
                t.join()

        elif data['action'] == 'presence':

            if data['user']['account_name'] in names:

                response = {
                    "response": 500,
                    "error": "Нет доступа"
                }

                response = json.dumps(response)
                response = response.encode()

                self.request.send(response)

                print('Ответ отправлен')

            else:

                account_name = data['user']['account_name']
                socks[account_name] = self.request

                user.user_name = account_name

                names.append(account_name)

                probe = {
                    "action": "probe",
                }

                probe = json.dumps(probe)
                probe = probe.encode()

                self.request.send(probe)

                print('Ответ отправлен')


class ClientClass:

    def __init__(self, ip, port):

        self._ip = ip
        self._port = port
        self.name = input('Введите ваше имя: ')

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect((self._ip, self._port))

        # ssl.wrap_socket(self.sock)

    def presence_message(self):

        presence = {
            "action": "presence",
            "type": "status",
            "user": {
                "account_name": self.name,
                "status": "Пользователь подключен"}
        }

        presence_json = json.dumps(presence)
        presence_buf = presence_json.encode()

        self.sock.send(presence_buf)

        result_buf = self.sock.recv(1024)
        result_json = result_buf.decode()
        result = json.loads(result_json)

        if result['action'] == 'probe':
            print('Вы вошли в чат')
        else:
            print(result['error'])


class JIMMessage(ClientClass):

    def send_msg(self):

        while True:

            message = input('>>> ')

            msg = {
                "action": "msg",
                "to": "account_name",
                "from": self.name,
                "encoding": "ascii",
                "message": message
            }

            msg = json.dumps(msg)
            msg = msg.encode()

            self.sock.send(msg)

            response = self.sock.recv(1024)

            print(response)
