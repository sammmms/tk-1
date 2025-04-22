# 🖥️ Computer Vision TK-1 Project 🚀  

*A step-by-step implementation of key CV techniques: Preprocessing, Edge Detection, Convolution, Morphology, and Feature Matching.*  

---

## 📋 Table of Contents  
1. [Project Overview](#-project-overview)  
2. [Dataset](#-dataset)  
3. [Techniques Implemented](#-techniques-implemented)

---

## 🌟 Project Overview  
This project demonstrates **5 core Computer Vision tasks** using both automated (OpenCV) and manual methods (matrix calculations). Key steps:  
- **Preprocessing** (Normalization)  
- **Edge Detection** (Sobel + Harris Corner)  
- **Convolution** (Gaussian Blur + Sobel)  
- **Morphology** (Dilation + Skeletonization)  
- **Feature Matching** (ORB + Brute-Force)  

---

## 📁 Dataset  
- **Source**: [Wiki-Art](https://www.wikiart.org/) / [Wiki-Art ART-GAN](https://github.com/cs-chan/ArtGAN/blob/master/WikiArt%20Dataset/README.md)  
- **Sample Size**: 50 images (e.g., `cat`, `car` classes)  
- **Preprocessing**: Normalization, 15x15 matrix sampling  

---

## 🛠️ Techniques Implemented  
| Task                | Method/Tool Used           |  
|---------------------|----------------------------|  
| Preprocessing       | OpenCV `cv2.normalize()`   |  
| Edge Detection      | Sobel Operator             |  
| Feature Detection   | Harris Corner              |  
| Noise Removal       | Gaussian Blur (3x3 kernel) |  
| Morphology          | Dilation + Skeletonization |  
| Feature Matching    | ORB + BFMatcher            |  

---
