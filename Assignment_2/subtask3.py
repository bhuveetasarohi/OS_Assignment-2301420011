# subtask3.py
# Subtask 3: Create and Execute Processes

import multiprocessing
import logging
from subtask2 import system_process

def run_processes():
    logging.basicConfig(filename='process_log.txt', level=logging.INFO)
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Both processes completed.")

if __name__ == "__main__":
    run_processes()
