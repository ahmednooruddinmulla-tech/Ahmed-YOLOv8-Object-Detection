"""Simple inference example for the supplied Ahmed YOLOv8 model."""
from pathlib import Path
from ultralytics import YOLO

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "ahmed_yolov8_best.pt"


def predict(source, conf=0.25, iou=0.45):
    """Run YOLO inference on an image, video, directory, or stream source."""
    model = YOLO(str(MODEL_PATH))
    return model.predict(source=source, conf=conf, iou=iou, verbose=False)


if __name__ == "__main__":
    print(f"Model: {MODEL_PATH}")
    print("Import predict(...) from this module or adapt the source argument for your input.")
