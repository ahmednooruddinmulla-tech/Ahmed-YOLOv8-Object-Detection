# Dataset directory

The full dataset is intentionally not included in this repository.

Expected prepared YOLO structure:

```text
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

The notebook can also start from the original class-folder dataset. Place that source dataset under `dataset_source/` before running the dataset preparation cells.
