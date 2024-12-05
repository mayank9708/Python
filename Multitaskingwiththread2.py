#Use a threading.lock to ensure only one thread accesses the resources at a time

import threading

lock = threading.lock()
counter = 0

def increment():
	global counter
	with lock:
		temp = counter
		temp += 1
		counter = temp
		print(f"Counter: {counter}")

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
	t.start()
for t in threads:
	t.join()
