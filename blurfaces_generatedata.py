#This script detects faces in datasets, then blurs the faces with different radius (from 1 to 15)
#And save the images to different folders (In this case, it will generate 15 different folders)
#As for now, it only works for 2017 coco datatset

#Parameter:
#	imagedir: directory of COCO dataset 2017
#	annotationdir: directory of keypoint annotation of COCO dataset 2017
#	outputdir: directory to store those new blurred datasets
#	upsample: non-negative integers. The higher the value, the smaller faces can be detected.

from pycocotools.coco import COCO
from PIL import Image, ImageFilter
import argparse
import os, json, time

import face_recognition

parser = argparse.ArgumentParser(description='Face detector and blurer')
parser.add_argument('--imagedir', type=str, default='./COCODatasets/val2017/')
parser.add_argument('--annotationdir', type=str, default='./COCODatasets/annotations/person_keypoints_val2017.json')
parser.add_argument('--outputdir', type=str, default='./COCODatasets/')
parser.add_argument('--upsample', type=int, default=2)

args = parser.parse_args()
image_dir = args.imagedir
annotation_dir = args.annotationdir
output_dirs = []
for i in range(1,16):
	output_dirs.append(args.outputdir + 'face_blurred_upsample_%s_radius_%s/' % (str(args.upsample),str(i)))

cocoGt = COCO(annotation_dir)
catIds = cocoGt.getCatIds(catNms=['person'])
keys = cocoGt.getImgIds(catIds=catIds)

for output_dir in output_dirs:
	try:
		os.mkdir(output_dir)
	except OSError as error:
		print(error)

start_time = time.time()
total_face_detected = 0

for key in keys:
	image_name = (12-len(str(key)))*'0' + str(key) + '.jpg'
	image = face_recognition.load_image_file(image_dir + image_name)
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=args.upsample, model="cnn")
	
	
	i=1
	for output_dir in output_dirs:
		pil_image = Image.fromarray(image)
		for face_location in face_locations:
			total_face_detected+=1
			top, right, bottom, left = face_location
			print("In image %s, a face is located at pixel location Top: %d, Left: %d, Bottom: %d, Right: %d" % (image_name, top, left, bottom, right))
			face_image = image[top:bottom, left:right]
			blurred_image = Image.fromarray(face_image).filter(ImageFilter.GaussianBlur(radius=i))
			try:
				pil_image.paste(blurred_image, (left, top))
			except ValueError as error:
				print(error)
		pil_image.save(output_dir + image_name)
		i+=1



# image = face_recognition.load_image_file("./COCODatasets/val2017/000000002299.jpg")
# face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=3, model="cnn")

# for face_location in face_locations:

#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#     print(face_location)
#     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
    