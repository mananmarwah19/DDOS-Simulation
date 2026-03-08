import requests
import threading

target = "http://127.0.0.1"

def send_requests():
    while True:
        try:
            r = requests.get(target)
            print("Request sent:", r.status_code)
        except Exception as e:
            print("Error:", e)

threads = []

for i in range(50):   # number of threads generating traffic
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)