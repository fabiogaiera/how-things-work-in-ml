import os
import sys
import numpy as np
from PIL import Image # Python Imaging Library


def resize_file_and_transform_to_array(path):
	
	size = 64, 64
	
	# Image.open method from PIL
	image = Image.open(path)
	image.thumbnail(size, Image.ANTIALIAS)

	#Removing the Alpha channel using Image.convert method from PIL
	image = image.convert("RGB")

	## This is the key routine that allows to convert from image to array.
	return np.array(image)


def reshape_matrix(path):
	img_matrix = resize_file_and_transform_to_array(path)
	img_matrix = img_matrix.reshape(img_matrix.shape[0] * img_matrix.shape[1] * img_matrix.shape[2], 1)
	img_matrix = img_matrix / 255 # Let's standardize the array
	return img_matrix


def show_image(path):
    return Image.open(path)