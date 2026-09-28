# Dataset Preparation

The project uses a 53-class custom object-detection dataset. The repository does not include the full image/label dataset.

The notebook expects the original class-folder dataset in `./dataset_source/` for the preprocessing stage, then creates a YOLO-format dataset in `./dataset/`.

See `configs/data.yaml` for the class mapping and train/validation paths.
