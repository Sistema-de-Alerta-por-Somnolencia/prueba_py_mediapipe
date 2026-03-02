from camera_thread import CameraThread
from worker_thread import WorkerThread
from shared import stop_event


if __name__ == "__main__":
    camera_thread = CameraThread()
    worker_thread = WorkerThread()

    camera_thread.start()
    worker_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nDeteniendo sistema...")
        stop_event.set()

        camera_thread.join()
        worker_thread.join()

        print("Sistema cerrado correctamente")