import socket
import time
import threading
import re
import sys


#pattern = r'/([a-zA-Z]+) (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) (\d+)|/([a-zA-Z]+)'
#p = re.compile(pattern)


#def join():
#    thread = threading.Thread(target=hello, daemon=True)
#    thread.start()
#    while True:
        

#def quit():
#    pass

#while True:
#    text=input()    
#    res=p.match(text)
#    if(res):
#        print(res.group(2)+":"+res.group(3)+" JOINED")
#        join()
port = sys.argv[1]
listenAddress = ('0.0.0.0', int(port))
def listen():
    with socket.socket() as s:
        s.bind(listenAddress)
        s.listen()
        while True:
            client, address= s.accept()
            with client:
                message = client.recv(2048).decode()
            print(address, message)

def main():
    address = None
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()
    while True:
        cmd = input('> ')
        if cmd.startswith('/'):
            tokens = cmd.split(' ')
            cmd=tokens[0]
            args = tokens[1:]
            if cmd == '/quit':
                break
            if cmd == '/join':
                print(args[0]+":"+args[1]+" JOINED")
                address = (args[0], int(args[1]))
        else:
            if address is None:
                print('JOIN FIRST')
                continue
            with socket.socket() as s:
                s.connect(address)
                s.send(cmd.encode())

if __name__=='__main__':
    print("Welcome to Messenger !")
    main()
