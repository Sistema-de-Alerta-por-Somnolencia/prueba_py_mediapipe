from ultralytics import YOLO
import cv2

# Cargar modelo entrenado
model = YOLO("best.pt")

# Imagen de prueba
imagen_path = "imagen_prueba.jpg"

# Ejecutar detección
results = model(imagen_path, conf=0.4)

# Mostrar resultados
for r in results:
    annotated_frame = r.plot()  # dibuja cajas

    cv2.imshow("Detecciones", annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()