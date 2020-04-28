## Result of Running Face Detection on Blurred Dataset
---

Model: **face_recognition**

Dataset: **COCO Dataset 2017 Validation**

### Format in 'detect_blurred_faces_upsample_#_radius_#.csv':
#### File Names:
- First `'#'`: The `upsample` value used to detect faces. In this folder, all face detection operation is based on `upsample = 2`.
- Second `'#'`: The `radius` of the Gaussian Blur when faces are being blurred. In this case, radius is from 1 to 20.


Each row in the file represents one face detection run.

For each row, the first element represents how many faces are detected from the entire dataset, 
using the specific upsample value. The second element indicates time consumed (in seconds) to run through the dataset.
