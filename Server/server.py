#echo-server-thread.py
import pyautogui
import socket
from _thread import *

HOST_IP='192.168.0.26'
HOST_PORT=10000

def my_com_th(client_socket, addr):
    #print('Client address: ',addr)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                #print('Client',addr, 'disconnected')
                break
            
            if   data.decode() =='a':
                pyautogui.keyDown('a')
                pyautogui.keyUp('a')
            elif data.decode() =='s':
                pyautogui.keyDown('s')
                pyautogui.keyUp('s')
            elif data.decode() =='d':
                 pyautogui.keyDown('d')
                 pyautogui.keyUp('d')
            elif data.decode() =='f':
                 pyautogui.keyDown('f')
                 pyautogui.keyUp('f')

            elif data.decode() =='e':
                 print('\nend')     
           
            #print('received from client is:', addr[0], data.decode())
        except ConnectionResetError as e:
            print('Client',addr[0], 'disconnected')
            break
    client_socket.close()
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST_IP,HOST_PORT))
server_socket.listen()
print("서버가 시작되었습니다.")
while True:
    client_socket, addr = server_socket.accept()
    start_new_thread(my_com_th, (client_socket, addr))
    
server_socket.close()
