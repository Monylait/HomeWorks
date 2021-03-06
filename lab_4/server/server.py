import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 9090))
serv_sock.listen(5)


def publick():
    with open('rsa_public.pem','r',encoding='utf-8') as pub_key:
        file=pub_key.read()
    return file


def private():
    with open('private_rsa_key.bin','r',encoding='utf-8') as priv_key:
        file=priv_key.read()
    return file



flag=True
while flag:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    #print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        #print(data)
        if not data:
            # Клиент отключился
            break
        if data == b'publick':
            b=publick().encode('utf-8')
            client_sock.sendall(b)
        elif data ==b'private':
            b=private().encode('utf-8')
            client_sock.sendall(b)
        elif data==b'Closed':
            flag=False
            break

    client_sock.close()