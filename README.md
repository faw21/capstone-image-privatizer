# Capstone Project -- Studying the Impact of Using Privatizers across Different Image-based Detection Tasks
---
This repository provides functionalities to estimate the impact of blurring faces on estimating human poses.

## My environment configuration:
- CUDA 10.0
- Tensorflow 1.14.0
- Python 3.6.9
- OpenCV 3
- etc

## Install

### Install CUDA 10.0 and CUDNN 7.6.5
---
### Install Python Dependencies
---
### Make pafprocess
---

- **run.py**: Evaluates human keypoints in a specific image and visualizes
- **eval.py**: Evaluates human keypoints in the dataset.
- **blurring.py**: Blurs the entire image within the dataset.
- **blurfaces_time_report.py**: detects and blurs faces within the dataset, and generates a csv file indicating how many faces does it detected and how long does it take to go through the dataset
- **blurfaces_generatedata.py**: detects and blurs faces within the dataset. Instead of only reporting the result of face detection, this script actually generates new datasets with the faces blurred.
- **eval_blurred.py**: Evaluates human keypoints in the blurred dataset.
- **detect_blurred_faces.py**: detects faces from blurred dataset, and stores the result in a csv file.

