from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

model.train(data="PPE-2-1/data.yaml", epochs=5, imgsz=416)
