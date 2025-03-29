import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pathlib import Path

IMAGE_DIR = "data/"
CLUSTERED_DIR = "clustered/"
NUM_CLUSTERS = 3  # Change as needed

def load_images(image_dir):
    images = []
    filenames = []
    for file in os.listdir(image_dir):
        if file.lower().endswith((".jpg", ".png")):
            path = os.path.join(image_dir, file)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (64, 64))
            images.append(img.flatten())
            filenames.append(path)
    return np.array(images), filenames

def cluster_images(features, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    return kmeans.fit_predict(features)

def save_clusters(labels, filenames):
    for i, label in enumerate(labels):
        cluster_folder = Path(CLUSTERED_DIR) / f"cluster_{label}"
        cluster_folder.mkdir(parents=True, exist_ok=True)
        filename = os.path.basename(filenames[i])
        img = cv2.imread(filenames[i])
        cv2.imwrite(str(cluster_folder / filename), img)

def visualize_samples(images, labels):
    plt.figure(figsize=(10, 6))
    for cluster_id in range(NUM_CLUSTERS):
        idx = np.where(labels == cluster_id)[0][:5]
        for i, img_id in enumerate(idx):
            plt.subplot(NUM_CLUSTERS, 5, cluster_id * 5 + i + 1)
            plt.imshow(images[img_id].reshape(64, 64), cmap='gray')
            plt.axis('off')
            plt.title(f"Cluster {cluster_id}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Loading images...")
    features, filenames = load_images(IMAGE_DIR)
    print("Clustering...")
    labels = cluster_images(features, NUM_CLUSTERS)
    print("Saving clustered images...")
    save_clusters(labels, filenames)
    print("Visualizing...")
    visualize_samples(features, labels)
