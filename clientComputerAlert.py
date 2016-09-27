import os
import socket
 #Ben Added to launch alert


#TCP send and receive functions written by Zach

def send(message,IP): #bytecode and string!
    TCP_IP = IP
    TCP_PORT = 8462 #Apple code requires port number higher than 1000
    BUFFER_SIZE = 1024
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Windows compliance
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1) #required for Apple compliance
        s.connect((TCP_IP,TCP_PORT))
        s.send(message)
        print('Sent')
    except:
        print('Failed to send')
        return False
    finally:
        s.close
        return True


def receive(IP):
    TCP_IP = IP
    TCP_PORT = 8462 #Apple code requires port number higher than 1000
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s = s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Windows compliance
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1) #Apple compliance
    s.bind((TCP_IP,TCP_PORT))
    s.listen(1)
    try:
        print('Waiting')
        c, addr = s.accept()
        data = c.recv(BUFFER_SIZE)
        print('Received')
        alert() #ben added to launch alert
        return data
    except:
        print('Failed to receive')
        return 0
    finally:
        c.close()

def monitor():
    while True:
        receive("")

def alert():
    print '\a\a'

#monitor code to call the functions
monitor()