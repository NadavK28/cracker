import socket
import threading
import sys
import webbrowser
import hashlib

class password:
    
    password = ""

def Generator(start, stop, md5):
    password.password=""
    for a in range(ord(start[0]),ord('z')+1):
        for b in range(ord(start[1]),ord('z')+1):
            for c in range(ord(start[2]),ord('z')+1):
                for d in range(ord(start[3]),ord('z')+1):
                    for e in range(ord(start[4]),ord('z')+1):
                        for f in range(ord(start[5]),ord('z')+1):
                            for g in range(ord(start[6]),ord('z')+1):
                                for h in range(ord(start[7]),ord('z')+1):
                                    st = chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)+chr(g)+chr(h)
                                    print(st)
                                    print(hashlib.md5(st.encode()).hexdigest())
                                    if hashlib.md5(st.encode()).hexdigest()==md5:
                                        password.password = st
                                    if (st==stop): 
                                        return
                                    

HOST = " "
PORT = 13370
START_MSG = "Howdy"
threads = []

def md5Decoder():
    pass

def initial(sock):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    return sock

def receiveReq(sock):
    while True:
        t = threading.Thread(target=handleConnection,args=(sock,sock.recv().decode(),))
        threads.append(t)

def handleConnection(sock,msg):
    if (msg =="Finished") :
        pass

    start,stop,md5 = msg.split(",")
    for char in range(len(start)):
        if start[char] != stop[char]:
            sum = int((ord(stop[char]) - ord(start[char])) / 3)
            #start[:char] + chr(ord(start[char]) + sum) + start[char+1:]
            lst = []
            lst.append(start)
            for i in range(3):
                lst.append(start[:char] + chr(ord(start[char]) + (sum * (i + 1))) + start[char+1:])
                threading.Thread(target=Generator(),args=(lst[i],lst[i+1],md5,))
            threading.Thread(target=Generator(),args=(lst[2],stop,md5,))
            print(lst)
            break

        
    # threading.Thread(target=Generator(),args=(start,lst[0],md5,))
    # threading.Thread(target=Generator(),args=(lst[0],lst[1],md5,))
    # threading.Thread(target=Generator(),args=(lst[1],lst[2],md5,))
    # threading.Thread(target=Generator(),args=(lst[2],stop,md5,))
    if (threads!=1):
        threads.pop()

    if md5Decoder()==True:
        sock.send("Found".encode())
        webbrowser.open("https://www.youtube.com/watch?v=cKULXMVCeOI")
        

def main():
    sock = initial()
    PORT = sock.recv().decode()
    sock.close()
    sock = initial()
    threading.Thread(target=receiveReq,args=(sock,))