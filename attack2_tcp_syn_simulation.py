import socket
import threading

target_ip = "127.0.0.1"
target_port = 80

def syn_simulation():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            print("Connection attempt sent")
            s.close()
        except:
            pass

threads = []

for i in range(100):
    t = threading.Thread(target=syn_simulation)
    t.start()
    threads.append(t)