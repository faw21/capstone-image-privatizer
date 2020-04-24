#This script measures the time to detect all faces in the dataset
#And generate a report showing how many face it detects, and how long it takes
#As for now, it only works for 2017 coco datatset

#Parameter:
#	imagedir: directory of COCO dataset 2017
#	annotationdir: directory of keypoint annotation of COCO dataset 2017
#	outputdir: directory to store those new blurred datasets
#	upsample: non-negative integers. The higher the value, the smaller faces can be detected.
#	times: non-negative integers. It determines how many times the model runs through the dataset.
#		Each time it generates a row of time report in the output csv file. The default is 1

from pycocotools.coco import COCO
from PIL import Image, ImageFilter
import argparse
import csv
import json, time

import face_recognition

parser = argparse.ArgumentParser(description='Face detector and blurer')
parser.add_argument('--imagedir', type=str, default='./COCODatasets/val2017/')
parser.add_argument('--annotationdir', type=str, default='./COCODatasets/annotations/person_keypoints_val2017.json')
parser.add_argument('--outputdir', type=str, default='./step2/')
parser.add_argument('--upsample', type=int, default=0)
parser.add_argument('--times', type=int, default=1)

args = parser.parse_args()
image_dir = args.imagedir
annotation_dir = args.annotationdir

cocoGt = COCO(annotation_dir)
catIds = cocoGt.getCatIds(catNms=['person'])
keys = cocoGt.getImgIds(catIds=catIds)

for i in range(0, args.times):
	start_time = time.time()
	total_face_detected = 0
	print('Running...')
	for key in keys:
		image_name = (12-len(str(key)))*'0' + str(key) + '.jpg'
		image = face_recognition.load_image_file(image_dir + image_name)
		face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=args.upsample, model="cnn")
		total_face_detected += len(face_locations)

	write_csv = args.outputdir + 'face_detection_time_report_upsample_%s.csv' % args.upsample
	total_time = time.time()-start_time
	with open(write_csv, 'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([total_face_detected, total_time])
	print('Finished!')
