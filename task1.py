import os

def parent_child():
    n = os.fork()
    if n > 0:  # Parent process
        print(f"Parent process, PID = {os.getpid()}, Child PID = {n}")
    else:  # Child process
        print(f"Child process, PID = {os.getpid()}, Parent PID = {os.getppid()}")

parent_child()



