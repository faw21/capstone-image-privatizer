## Result of Running Pose Estimation on Original Dataset
---

Model: **CMU**

Dataset: **COCO Dataset 2017 Validation**

Resolution: From **96x96** to **496x496**. The resolution information is shown in the file names

#### Format in 'cmu_coco2017_###x###.json':
This kind of file contains all estimated keypoint coordinates for each image in the dataset.

It consists a list of dictionaries. Each dictionary stores estimation result of one image. 
The format of `keypoints` section within each dictionary is [x1, y1, v1, x2, y2, v2, ..., xk, yk, vk], 
where x,y are the keypoint locations and v is a visibility flag defined as 
v=0: not labeled, v=1: labeled but not visible, and v=2: labeled and visible.

#### Format in 'estimation_result_cmu_coco2017_###x###.csv':
This kind of file contains metrics that used to characterize the performance of the pose estimation.

Each row represents one run.

Within each row of the file, the first 5 elements are average precisions (0<AP<1), 6th ~ 10th elements are average recalls (0<AR<1), 
and the last element (11th) is the time (in seconds) to run the pose estimation through the dataset.

The explanation of each Average Precision/Average Recall is [here](http://cocodataset.org/#keypoints-eval)
