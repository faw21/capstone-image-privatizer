# Capstone Project -- Studying the Impact of Using Privatizers across Different Image-based Detection Tasks

This repository provides functionalities to learn the impact of blurring faces on estimating human poses.

## My environment configuration:
- CUDA 10.0
- Tensorflow 1.14.0
- Python 3.6.9
- OpenCV3
- etc

**Note that this repository works with COCO Dataset and Tensorflow. The COCO evaluation package does not provide support for Windows, and the Tensorflow does not provide GPU acceleration for Mac OS. So Ubuntu is recommended.**

## Installation
### Install Python Dependencies
Clone the repo.
```
$ git clone https://github.com/faw21/capstone-image-privatizer.git
$ cd capstone-image-privatizer
```

Install CMake and other python dependencies.

```
$ sudo apt-get install cmake
$ pip3 install cython
$ pip3 install numpy==1.17.1
$ pip3 install -r requirements.txt
```

The previous step will install the latest version of numpy for you, while this repository requires numpy 1.17.1. For some reason, some environments allow multiple versions of numpy to co-exist. To make sure you are using the 1.17.1, REPEAT `pip3 uninstall numpy` until nothing shows up when you type `pip3 show numpy`, then install the numpy==1.17.1
```
$ pip3 uninstall numpy
$ pip3 install numpy==1.17.1
```

### Download Tensorflow Graph File(pd File)
There are 4 pose estimation models available in this repo:

- cmu
- mobilenet_thin
- mobilenet_v2_large
- mobilenet_v2_small

CMU's model graph file is too large for git, so it was uploaded to an external cloud. You should download them before using it. Download scripts are provided in the model folder.

```
$ cd models/graph/cmu
$ bash download.sh
```
### Demo
Now the repo is installed. You can try the following demo:
```
$ python3 run_pose.py --model=cmu --resize=656x368 --image=./images_demo/apink1.jpg
$ python3 run_face.py --radius=15 --image_dir=./images_demo/apink1.jpg
```

### Install Nvidia driver, CUDA=10.0, and CUDNN>=7.6.5
If you have not installed the CUDA and CUDNN, you can only execute the face detection model and pose estimation model using CPU, which is super slow. Install CUDA and CUDNN to your machine to get GPU support. **The Tensorflow-GPU 1.14.0 only works with CUDA 10.0**.

### Acquire dataset
You can download the [2017 COCO Validation Dataset](http://images.cocodataset.org/zips/val2017.zip) and the corresponding [annotation](http://images.cocodataset.org/annotations/annotations_trainval2017.zip), which I used on this repo. You can also check out other versions of COCO dataset here: http://cocodataset.org/#download

- **eval.py**: Evaluates human keypoints in the dataset.
- **blur_entire_image.py**: Blurs the entire image within the dataset.
- **blurfaces_time_report.py**: detects and blurs faces within the dataset, and generates a csv file indicating how many faces does it detected and how long does it take to go through the dataset
- **blurfaces_generatedata.py**: detects and blurs faces within the dataset. Instead of only reporting the result of face detection, this script actually generates new datasets with the faces blurred.
- **eval_blurred.py**: Evaluates human keypoints in the blurred dataset.
- **detect_blurred_faces.py**: detects faces from blurred dataset, and stores the result in a csv file.

