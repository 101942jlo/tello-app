#import
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_Addres = ('192.168.10.1', 8889)
sock.bind(('', 8889))

while True:
    try:
        msg = input('insert command: \n')
        if not msg:
            break
        if 'end' in msg:
            sock.close()
            break
        msg = msg.encode()
        sent = sock.sendto(msg, tello_Addres)
    except Exception as err:
        print(err)
        sock.close()
        break