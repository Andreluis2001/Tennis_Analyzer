from ultralytics import YOLO

model = YOLO("yolov8x")

model.predict(source="input_videos/input_video.mp4", save=True)