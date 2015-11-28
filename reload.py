from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time                          
           
class FileModifiedHandler(FileSystemEventHandler):

    def __init__(self, path, file_name, callback):
        self.file_name = file_name
        self.callback = callback

        self.observer = Observer()
        self.observer.schedule(self, path, recursive=False)
        self.observer.start()
        self.observer.join()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.file_name):
            # self.observer.stop()
            self.callback() # call callback


if __name__ == '__main__':
    from sys import argv, exit
    MESSG = 'Press CTRL+SHIFT+\ to exit...'
    if not len(argv) <= 2:
        print("Usage: reload <filename> <optional_args>")
        exit(1)
    print(MESSG)
        
    def callback(tell=True):
        bashCommand = "xelatex {filename}".format(filename=argv[1])
        import subprocess
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        if tell:
            print output, '\n', MESSG

    FileModifiedHandler('.', argv[1], callback)
