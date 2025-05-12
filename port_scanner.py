import socket

target = '192.168.1.1'
ports = [22, 80, 443]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f'Port {port} is open')
    s.close()
