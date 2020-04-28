## Result of Running Face Detection on Original Dataset
---

Model: **face_recognition**

Dataset: **COCO Dataset 2017 Validation**

#### Format in 'face_detection_time_report_upsample_#.csv':
The `#` represents the upsample value. (upsample = 0~2).

`upsample`: It is a parameter of the face detection model. Higher values find smaller faces.

Each row in the file represents one face detection run.

For each row, the first element represents how many faces are detected from the entire dataset, 
using the specific upsample value. The second element indicates time consumed (in seconds) to run through the dataset.
