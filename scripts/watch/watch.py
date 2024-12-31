import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class PyFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(self.file_name):
            print(f"\nFile changed! Running {self.file_name}...")
            subprocess.run(['python', self.file_name], cwd=os.path.dirname(__file__))

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python watch.py <file_name>")
        sys.exit(1)

    file_to_watch = sys.argv[1]
    event_handler = PyFileHandler(file_to_watch)
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