import socket

print('hi')

addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
s = socket.socket()
s.bind(('0.0.0.0', 8080))
s.listen(3)
print('Listening: ',addr )


try:
    while True:
        con, add = s.accept()
        print(con, add)
        data = con.recv(1024)
        print(data)
        con.send(b'HTTP/1.0 200 OK\r\nContrnt-type: text/html\r\n\r\n')
        con.sendall(b'hi')
        con.sendall(data)
        print('find:   ', data.decode().find('19254')) 
finally:
    s.close()