import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# BINDING SOCKET WITH LOCALHOST AND PORT
sock.bind(('127.0.0.1', 8081))

# LISTENING FOR CONNECTION
print("""
    Started listening for connection.
""")
sock.listen()
conn, addr = sock.accept()


# ACKNOWLEDGE CONNECTION
print(addr, 'connected.')
conn.send('You are now connected.\n'.encode('utf-8'))


with conn:
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            data = [int(x) for x in data]
            my_sum = sum(data)
            conn.sendall(str(my_sum).encode('utf-8'))
        except ConnectionAbortedError:
            print(f'Connection lost.')
            break
        except NameError:
            print(f'There was an error.\n{NameError}')
