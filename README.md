# 🧠 Computer Vision: Object Detection & Segmentation

A comprehensive image processing project for analyzing, identifying, and segmenting objects using modern Computer Vision techniques.

---

## 📚 Table of Contents

- [🧠 Computer Vision: Object Detection \& Segmentation](#-computer-vision-object-detection--segmentation)
  - [📚 Table of Contents](#-table-of-contents)
  - [📌 Overview](#-overview)
  - [🗂️ Dataset](#️-dataset)
  - [🧪 Techniques Implemented](#-techniques-implemented)
  - [💻 How to Run](#-how-to-run)
  - [📍 Conclusion](#-conclusion)

---

## 📌 Overview

This project explores a series of computer vision techniques, including preprocessing, segmentation, feature detection, convolution, morphology, and feature matching. The objective is to identify and isolate objects from images efficiently, using various well-established methods.

---

## 🗂️ Dataset

- 📦 **Source**: COCO (Common Objects in Context)
- 📈 **Images**: ~100 images (configurable)

Images are preprocessed and used throughout the notebook to test and visualize the effect of each technique.

---

## 🧪 Techniques Implemented

| **Category**              | **Techniques**                                                                |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Preprocessing**         | Grayscale Conversion, Normalization, Contrast Enhancement (CLAHE), Sharpening |
| **Segmentation**          | Thresholding (Binary, Adaptive), Canny Edge Detection                         |
| **Feature Detection**     | Harris Corner Detection, SIFT, ORB                                            |
| **Convolution (Noise)**   | Gaussian Blur, Median Filter                                                  |
| **Convolution (Enhance)** | Prewitt, Sobel, Laplacian                                                     |
| **Morphological Ops**     | Dilation, Erosion, Opening, Closing, Hole Filling, Skeletonization            |
| **Feature Matching**      | Brute-Force Matcher (Hamming for ORB, L2 for SIFT)                            |

---

## 💻 How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/sammmms/tk-1.git
   cd tk-1
   ```
2. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook
   ```bash
   jupyter notebook tk-1.ipynb
   ```

## 📍 Conclusion

This project demonstrates a full workflow of image analysis using computer vision. By applying multiple processing and analysis techniques, we successfully segmented and identified various objects from real-world image datasets, laying the groundwork for further development in CV applications.
