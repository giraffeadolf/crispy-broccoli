from subprocess import Popen, CREATE_NEW_CONSOLE

process_list = []

while True:
    user = input("Запустить 3 клиента (s)\nЗакрыть клиентов (x)\nВыйти (q)\n")

    if user == 'q':
        break
    elif user == 's':
        for _ in range(3):
            process_list.append(Popen('python client.py', creationflags=CREATE_NEW_CONSOLE))
            print('Запущено 3 клиента')
    elif user == 'x':
        for p in process_list:
            p.kill()
        process_list.clear()
