from PIL import Image, ImageFilter
import argparse
import face_recognition

parser = argparse.ArgumentParser(description='Face detector and blurer demo')
parser.add_argument('--image', type=str, default='./images_demo/apink1.jpg')
parser.add_argument('--radius', type=int, default=10)

args = parser.parse_args()
image = face_recognition.load_image_file(args.image)
face_locations = face_recognition.face_locations(image, model='cnn')

pil_image = Image.fromarray(image)
for face_location in face_locations:

#Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    blurred_image = Image.fromarray(face_image).filter(ImageFilter.GaussianBlur(radius=args.radius))
    pil_image.paste(blurred_image, (left, top))
pil_image.show()
    
