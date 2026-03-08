import threading
##Crea una bandera global que permite detener todos los hilos sin forzarlos.
stop_event = threading.Event()