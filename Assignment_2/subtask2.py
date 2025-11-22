# subtask2.py
# Subtask 2: Define System Process Function

import time
import logging

def system_process(task_name):
    """Simulates a system process performing a small task."""
    logging.info(f"{task_name} started")
    time.sleep(2)
    logging.info(f"{task_name} ended")

if __name__ == "__main__":
    logging.basicConfig(filename='process_log.txt', level=logging.INFO)
    system_process("DemoProcess")
    print("System process executed. Check process_log.txt.")
