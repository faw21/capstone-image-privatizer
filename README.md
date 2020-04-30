# Capstone Project -- Studying the Impact of Using Privatizers across Different Image-based Detection Tasks

This repository provides functionalities to learn the impact of blurring faces on estimating human poses.

## My environment configuration:
- CUDA 10.0
- Tensorflow 1.14.0
- Python 3.6.9
- OpenCV 3
- etc

## Installation
### Install Python Dependencies
Clone the repo and install 3rd-party libraries.
```
$ git clone https://github.com/faw21/capstone-image-privatizer.git
$ cd capstone-image-privatizer
$ pip3 install -r requirements.txt
```
This repository requires numpy 1.17.1. If you already have another version of numpy installed, **MAKE SURE UNINSTALL IT FIRST THEN INSTALL 1.17.1**.
```
$ pip3 uninstall numpy
$ pip3 install numpy==1.17.1
```

### Install CUDA 10.0 and CUDNN 7.6.5
---

### Make pafprocess
---

- **run.py**: Evaluates human keypoints in a specific image and visualizes
- **eval.py**: Evaluates human keypoints in the dataset.
- **blur_entire_image.py**: Blurs the entire image within the dataset.
- **blurfaces_time_report.py**: detects and blurs faces within the dataset, and generates a csv file indicating how many faces does it detected and how long does it take to go through the dataset
- **blurfaces_generatedata.py**: detects and blurs faces within the dataset. Instead of only reporting the result of face detection, this script actually generates new datasets with the faces blurred.
- **eval_blurred.py**: Evaluates human keypoints in the blurred dataset.
- **detect_blurred_faces.py**: detects faces from blurred dataset, and stores the result in a csv file.

