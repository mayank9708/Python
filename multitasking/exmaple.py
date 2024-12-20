import threading
import  time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for char in 'ABCDE':
        print(f"Letter: {char}")
        time.sleep(1)

# create threads
t2 = threading.Thread(target=print_letters)
t1 = threading.Thread(target=print_numbers)

# start threads
t1.start()
t2.start()

# wait for both threads to completel
t1.join()
t2.join()
