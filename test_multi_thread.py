import threading
import time

def task(name, seconds):
    time.sleep(seconds)  # Blocking (CPU-bound)
    print(f"{name} start")
    print(f"{name} finished after {seconds} seconds.")
    print(f"{name} end")

thread1 = threading.Thread(target=task, args=("Task 1", 2))
thread2 = threading.Thread(target=task, args=("Task 2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
