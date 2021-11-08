#echo-client.py
import socket
import RPi.GPIO as g
import time
IN_TOUCH1 = 4 # GPIO 4
IN_TOUCH2 = 17 # GPIO 17
IN_TOUCH3 = 27 # GPIO 27
IN_TOUCH4 = 22 # GPIO 22
IN_TOUCH5 = 5 # GPIO 5
close1 = 0

g.setmode(g.BCM)
g.setup(IN_TOUCH1, g.IN)
g.setup(IN_TOUCH2, g.IN)
g.setup(IN_TOUCH3, g.IN)
g.setup(IN_TOUCH4, g.IN)
g.setup(IN_TOUCH5, g.IN)

HOST_IP = '192.168.0.24'
PORT = 10000

def call1(channl):
    global HOST_IP, PORT, close1
    if close1 == 0:
        client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client_socket.connect((HOST_IP, PORT))
        close1 = 1
    while True:
        value = g.input(IN_TOUCH1)
        client_socket.sendall("a".encode())
        if value == 0:
            client_socket.sendall("quit".encode())
            break
    client_socket.close()
    close1 = 0
def call2(channl):
    global HOST_IP, PORT, close1
    if close1 == 0:
        client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client_socket.connect((HOST_IP, PORT))
        close1 = 1
    while True:
        value = g.input(IN_TOUCH2)
        client_socket.sendall("s".encode())
        if value == 0:
            client_socket.sendall("w".encode())
            break
    client_socket.close()
    close1 = 0
def call3(channl):
    global HOST_IP, PORT, close1
    if close1 == 0:
        client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client_socket.connect((HOST_IP, PORT))
        close1 = 1
    while True:
        value = g.input(IN_TOUCH3)
        client_socket.sendall("d".encode())
        if value == 0:
            client_socket.sendall("r".encode())
            break
    
    client_socket.close()
    close1 = 0
def call4(channl):
    global HOST_IP, PORT, close1
    
    if close1 == 0:
        client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client_socket.connect((HOST_IP, PORT))
        close1 = 1
    while True:
        value = g.input(IN_TOUCH4)
        client_socket.sendall("f".encode())
        if value == 0:
            client_socket.sendall("t".encode())
            break
    client_socket.close()
    close1 = 0
def call5(channl):
    global HOST_IP, PORT
    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client_socket.connect((HOST_IP, PORT))
    client_socket.sendall("e".encode())
    client_socket.close()
    global a
    a = 1

    
    

g.add_event_detect(IN_TOUCH1, g.RISING, callback=call1)
g.add_event_detect(IN_TOUCH2, g.RISING, callback=call2)
g.add_event_detect(IN_TOUCH3, g.RISING, callback=call3)
g.add_event_detect(IN_TOUCH4, g.RISING, callback=call4)

g.add_event_detect(IN_TOUCH5, g.BOTH, callback=call5)

a = 0




    
        
print ("Start")
while True:
    time.sleep(0.1)
    if a == 1:
        break


    
    
        
