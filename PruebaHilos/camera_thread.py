import threading
import cv2
import time
from shared import stop_event


class CameraThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)

    def run(self):
        prev_time = time.time()

        while not stop_event.is_set():
            ret, frame = self.cap.read()

            if not ret:
                print("No se pudo leer la cámara")
                break

            # Calcular FPS
            current_time = time.time()
            fps = 1 / (current_time - prev_time)
            prev_time = current_time

            print(f"FPS: {fps:.2f}")

        self.cap.release()
        print("Cámara liberada")