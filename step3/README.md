## Result of Running Pose Estimation on Blurred Dataset
---

Model: **CMU**

Dataset: **COCO Dataset 2017 Validation**

Resolution: **432x368**.



### Format of File Names:
- `432x368` indicates the resolution of the dataset
- First `'#'`: The `upsample` value used to detect faces. In this folder, all face detection operation is based on `upsample = 2`.
- Second `'#'`: The `radius` of the Gaussian Blur, In this case, radius was selected from 1 to 20.

      `radius`: A parameter of Gaussian Blur. It determines how much the image is blurred. Higher value represents more intensive blurring.

### The content of files have the same format as the files in step1 folder. See its [README.md](https://github.com/faw21/capstone-image-privatizer/tree/master/step1)
