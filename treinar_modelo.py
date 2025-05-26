from ultralytics import YOLO

# Criar modelo base
model = YOLO("yolov8n.pt")  # podes usar yolov8s.pt se quiseres mais precisão

# Treinar com o dataset
model.train(data="PPE-2-1/data.yaml", epochs=5, imgsz=416)
