# subtask4.py
# Subtask 4: Full System Simulation (Startup → Execution → Shutdown)

from subtask1 import init_logging
from subtask3 import run_processes

if __name__ == "__main__":
    print("System Starting...")
    init_logging()
    run_processes()
    print("System Shutdown.")
