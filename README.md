# Ahmed — Custom Object Detection with YOLOv8

An end-to-end custom object-detection project using **YOLOv8l**. The project covers dataset inspection and conversion, model training, fine-tuning, evaluation, visualization, and model export/deployment experiments.

## Project highlights

- Custom **53-class** object-detection dataset
- YOLO-format dataset preparation with train/validation split
- YOLOv8l training for **100 epochs** with early stopping
- Fine-tuning with a lower learning rate
- Evaluation using mAP@0.5, mAP@0.5:0.95, precision, and recall
- Confusion matrices, F1, precision-confidence, recall-confidence, and precision-recall curves
- Sample training/validation visualizations
- PyTorch model supplied as a Git LFS-managed `.pt` file
- Basic inference helper included in `src/inference.py`

## Repository structure

```text
Ahmed-YOLOv8-Object-Detection/
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
├── notebooks/
│   └── Ahmed_ObjectDetection_YOLOv8.ipynb
├── configs/
│   ├── data.yaml
│   └── args.yaml
├── models/
│   └── ahmed_yolov8_best.pt
├── results/
│   ├── results.csv
│   ├── results.png
│   ├── baseline_vs_finetune.png
│   ├── F1_curve.png
│   ├── precision_confidence_curve.png
│   ├── precision_recall_curve.png
│   ├── recall_confidence_curve.png
│   ├── confusion_matrix.png
│   ├── confusion_matrix_normalized.png
│   └── labels.jpg
├── examples/
├── dataset/
│   └── README.md
├── src/
│   └── inference.py
└── docs/
    ├── DATASET.md
    └── MODEL_CARD.md
```

## Recorded training configuration

The supplied training configuration records:

| Parameter | Value |
|---|---:|
| Model | YOLOv8l |
| Epochs | 100 |
| Image size | 640 × 640 |
| Batch size | 16 |
| Optimizer | AdamW |
| Early stopping patience | 15 |
| Initial learning rate | 0.001 |
| Validation | Enabled |
| Mixed precision (AMP) | Enabled |

## Recorded results

The final row of the supplied `results.csv` records:

| Metric | Value |
|---|---:|
| Precision | 0.85108 |
| Recall | 0.80764 |
| mAP50 | 0.85867 |
| mAP50-95 | 0.66356 |

A separate supplied comparison figure reports baseline vs fine-tuned results and is included under `results/`.

## Installation

Create a Python environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Jupyter:

```bash
python -m ipykernel install --user --name=ahmed-yolov8 --display-name="Python (Ahmed YOLOv8)"
jupyter notebook
```

## Dataset

The full dataset is **not included** in this repository. The notebook's preprocessing stage expects the original class-folder dataset under:

```text
./dataset_source/
```

It then creates the prepared YOLO dataset under:

```text
./dataset/
```

See `docs/DATASET.md` and `configs/data.yaml`.

## Model download / Git LFS

The supplied PyTorch model is about 88 MB, so it is configured for Git LFS.

Install Git LFS once:

```bash
brew install git-lfs

git lfs install
```

Then clone the repository normally; Git LFS will fetch the model file.

## Example inference

```python
from src.inference import predict

results = predict("path/to/image.jpg")
results[0].save()
```

## Academic / project note

This repository contains the author's implementation, experiments, evaluation artifacts, and supplied trained model. Results are specific to the dataset and experimental configuration used in the project.
