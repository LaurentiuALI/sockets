import socket

x = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ENSURE CONNECTION
sock.connect(('localhost', 8081))

# LISTEN FOR SUCCESSFUL CONNECTION
response = sock.recv(1024)
print(response.decode('utf-8'))

try:
    x = 1
    while x != 0:
        print("""
            We will make the server make some simple addition.
            Please enter two number and the server will handle the rest.
            If you want to stop, write 0 at any point.
        """)

        input_1 = int(input("Write the first number: "))
        if input_1 == 0:
            break

        input_2 = int(input("Write the second number: "))
        if input_2 == 0:
            break

        sock.send(f'{input_1}{input_2}'.encode('utf-8'))

        print(f'The answer from server is: {sock.recv(1024).decode("utf-8")}')

    sock.close()


except NameError:
    print(f'An error occurred, namely\n{NameError}')
