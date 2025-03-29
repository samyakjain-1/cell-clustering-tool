# 🧠 Cell Image Clustering Tool

A lightweight, Dockerized machine learning tool to automatically cluster microscopy or biomedical images based on visual similarity. Built using Python, OpenCV, and scikit-learn, this tool enables fast, unsupervised grouping of unlabeled cell images — helping researchers streamline data preparation and labeling.

---

## 🚀 Features

- Clusters images using K-Means with pixel-level feature vectors
- Supports grayscale or RGB-based clustering
- Saves output to organized folders (`cluster_0/`, `cluster_1/`, etc.)
- Visualizes clustered image groups with matplotlib
- Fully containerized with Docker for easy reproducibility

---

## 🧰 Technologies Used

- Python 3.11
- OpenCV for image loading and preprocessing
- NumPy for vectorization
- Scikit-learn for K-Means clustering and (optional) PCA
- Matplotlib for visual inspection of cluster results
- Docker for containerization and reproducibility

---

## 🧪 How It Works

1. Reads all `.jpg` or `.png` images from the `data/` folder
2. Converts images to grayscale or uses raw RGB (optional)
3. Resizes images to 64×64 and flattens them into feature vectors
4. Applies unsupervised clustering using K-Means
5. Saves results into separate `cluster_X` folders and displays a visualization

---

## 🐳 Docker Quickstart

Build the Docker image:
```bash
docker build -t cell-cluster-app .
```

Run the container (with mounted folders):
```docker run -it \
  -v "$PWD/data:/app/data" \
  -v "$PWD/clustered:/app/clustered" \
  cell-cluster-app
```
📂 Images should be placed in the data/ folder before running.
