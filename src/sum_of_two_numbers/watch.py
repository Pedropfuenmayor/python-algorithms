import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class PyFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('sum_of_two_numbers.py'):
            print("\nFile changed! Running sum_of_two_numbers.py...")
            subprocess.run(['python', 'sum_of_two_numbers.py'], cwd=os.path.dirname(__file__))

if __name__ == "__main__":
    event_handler = PyFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(__file__), recursive=False)
    observer.start()

    try:
        print("Watching for changes in sum_of_two_numbers.py... (Press Ctrl+C to stop)")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 