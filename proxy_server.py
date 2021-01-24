#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8080
BUFFER_SIZE = 512

def handle_process(conn, addr, s):
    full_data = conn.recv(BUFFER_SIZE)
    print(full_data)
    s.sendall(full_data)
    s.shutdown(socket.SHUT_WR)
    full_data = s.recv(BUFFER_SIZE)
    print(full_data)
    conn.send(full_data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
           
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                 #connect to google.com
                IP = socket.gethostbyname("www.google.com")
                s2.connect((IP , 80))

                p = Process(target=handle_process, args=(conn, addr, s2))
                p.daemon = True
                p.start()

                time.sleep(0.5)
            conn.close()

if __name__ == "__main__":
    main()
