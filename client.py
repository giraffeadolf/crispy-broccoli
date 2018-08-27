from methods import JIMMessage

client = JIMMessage('127.0.0.1', 7777)

client.presence_message()
client.send_msg()
