import psutil
import time

# Specify the list of process names to kill
PROCESS_NAMES = ['netwiz.exe', 'bzjwhfivlx.exe','notepad.exe']

def kill_process_by_names(process_names):
    """Kill all processes with the specified names."""
    
    # Flag to indicate if any process was killed
    killed_any = False  

    # Iterate over all running processes
    for process in psutil.process_iter(['name']):
        try:
            # Check if process name matches
            if process.info['name'] in process_names:
                print(f"Killing process: {process.info['name']} (PID: {process.pid})")
                process.kill()  # Kill the process
                killed_any = True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Handle the case where the process may have ended or access is denied
            continue
            
    return killed_any

def main():
    try:
        print(f"Monitoring for processes: {', '.join(PROCESS_NAMES)}. Press Ctrl+C to stop.")
        
        while True:
            killed = kill_process_by_names(PROCESS_NAMES)
            if not killed:
                print(f"No running processes found among: {', '.join(PROCESS_NAMES)}.")           
            time.sleep(1)  # Wait for 1 second before checking again
            
    except KeyboardInterrupt:
        print("\nExiting the monitor. Goodbye!")
        
if __name__ == "__main__":
    main()