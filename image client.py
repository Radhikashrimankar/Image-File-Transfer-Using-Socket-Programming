import socket
s = socket.socket()
host = socket.gethostname()
port = 

s.connect((host, port))
s.send(b"Hello server!")

with open('i-client.jpg', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(4096)
        print('data=%s', (data))
        if not data:
            break

        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
