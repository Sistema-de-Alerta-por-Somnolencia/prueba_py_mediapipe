import threading
import time
from shared import stop_event


class WorkerThread(threading.Thread):
    def run(self):
        while not stop_event.is_set():
            print("Worker activo")
            time.sleep(3)

        print("Worker detenido")