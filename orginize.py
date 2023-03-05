import sys
import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\Max laptop\Downloads\from_dir"
to_dir= "C:\Users\Max laptop\Downloads\to_dir"

dir_tree = {
    "Image_Files": ['.jpg','.jpeg','.png','.jif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls','.xlsx', '.csv', '.pdf', '.txt' ],
    "Setup_Files": ['.exe', '.bin', '.cmd','.msi', '.dmg',]
}

#event handler class
class FileMovementHandeler(FileSystemEventHandler):

    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)

        time.sleep(1)

event_handler = FileMovementHandeler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()