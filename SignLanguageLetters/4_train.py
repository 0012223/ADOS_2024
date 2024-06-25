from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

if __name__ == "__main__":
	results = model.train(
		data = "data.yaml",
		imgsz = 640,
		epochs = 100,
		plots = True,
		device = 0
	)
