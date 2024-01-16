#import
import threading
import time
import socket


# def func1():
#     print("Func 1")
#     time.sleep(2)
#     print("Func 1")

# def func2():
#     print("Hola 2")
#     time.sleep(4)
#     print("hola 2")

# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)

# t1.start()
# t2.start()


# t1.join()

# print("finish")


def sendCommand():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_Addres = ('192.168.10.1', 8889)
    sock.bind(('', 8889))
    sock.sendto("command".encode(), tello_Addres)

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
            # output the response (if any)
            data, ip = sock.recvfrom(1024)
            print(data)
            print("{}: {}".format(ip, data.decode()))
        except Exception as err:
            print(err)
            sock.close()
            break

def stats():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_IP = ""
    udp_PORT = 8890
    sock.bind((udp_IP, udp_PORT))

    while True:
        try:
            print('hello')
            print('hellqqqw')
            data, addr = sock.recvfrom(1024)
            print('hello2')
            print(data)
            print(data.decode())

        except Exception as err:
            print(err)
            sock.close()
            break

t1 = threading.Thread(target=sendCommand)
t2 = threading.Thread(target=stats)

t1.start()
# t2.start()