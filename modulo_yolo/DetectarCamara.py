from ultralytics import YOLO
import cv2

# Cargar modelo entrenado
model = YOLO("best.pt")

# Abrir cámara (0 = webcam principal)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Ejecutar detección
    results = model(frame, conf=0.4)

    # Dibujar resultados
    annotated_frame = results[0].plot()

    cv2.imshow("Deteccion YOLO", annotated_frame)

    # Presiona Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()