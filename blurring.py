### This script blurs entire images and save them
#Parameters:
#	radius: The radius of Gaussian Blur. The higher the value the more intensive the images are blurred.
#	cocodir: The directory of coco dataset.
#	outputdir: Output directory
#	cocoyear: 2014 or 2017. Determines the dataset version.
from pycocotools.coco import COCO
from PIL import Image, ImageFilter
import argparse
import json
import os

parser = argparse.ArgumentParser(description='COCO Image Blurring')
parser.add_argument('--radius', type=int, default=2)
parser.add_argument('--cocodir', type=str, default='./COCODatasets/')
parser.add_argument('--outputdir', type=str, default='./COCODatasets/')
parser.add_argument('--cocoyear', type=str, default='2017')

args = parser.parse_args()

image_dir = args.cocodir + 'val%s/' % args.cocoyear
coco_json_file = args.cocodir + 'annotations/person_keypoints_val%s.json' % args.cocoyear

cocoGt = COCO(coco_json_file)
catIds = cocoGt.getCatIds(catNms=['person'])
keys = cocoGt.getImgIds(catIds=catIds)
outputdirectory = args.outputdir + 'GaussianBlur_%s/val%s/' % (str(args.radius), args.cocoyear) 
try:
	os.mkdir(args.outputdir + 'GaussianBlur_%s/' % (str(args.radius)))
except OSError as error:
	print(error)
try:
	os.mkdir(outputdirectory)
except OSError as error:
	print(error)


for key in keys:
	image_name = (12-len(str(key)))*'0' + str(key) + '.jpg'
	image = Image.open(image_dir + image_name)
	image = image.filter(ImageFilter.GaussianBlur(radius=2))
	image.save(outputdirectory + image_name)
