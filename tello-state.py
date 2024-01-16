#import
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_IP = "0.0.0.0"
udp_PORT = 8890
sock.bind((udp_IP, udp_PORT))

while True:
    try:
        print('hello')
        data, addr = sock.recvfrom(1024)
        print('hello2')
        print(data)
        print(data.decode())

    except Exception as err:
        print(err)
        sock.close()
        break