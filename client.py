import socket
import threading

locking = threading.Lock()
closed = False

def receving(name, sock):
    while not closed:
        try:
            locking.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
        except:
            pass
        finally:
            locking.release()

host = socket.gethostname()
port = 6666

server = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))
s.setblocking(0)

recvThread = threading.Thread(target=receving, args=("RecvThread",s))
recvThread.start()

s.sendto("New user",server)
message = raw_input("Insert message: ")

while message != 'escape':
    if message != '':
        s.sendto(message, server)
    locking.acquire()
    message = raw_input("Insert message: ")
    locking.release()

s.sendto("New user connected",server)

inchis = True
recvThread.join()
s.close()
