# Model Card — Ahmed YOLOv8 Object Detection

## Model

YOLOv8l-based custom object detector trained for 53 object classes.

## Training configuration

The supplied training configuration records 100 epochs, a 640-pixel image size, batch size 16, AdamW optimization, validation enabled, mixed precision, and early stopping patience of 15. See `configs/args.yaml` for the complete recorded configuration.

## Included model

`models/ahmed_yolov8_best.pt` is the model file supplied with this project.

## Intended use

Academic/research experimentation, object detection evaluation, and prototype deployment.

## Limitations

Performance depends on the training data, class balance, scene conditions, camera characteristics, and deployment environment. The full training dataset is not redistributed in this repository.
