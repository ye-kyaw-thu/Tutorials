import sys
import cv2
import numpy as np
import caffe
import glob
import os, os.path

# for feature extraction
# I called this program from a bash shell script named "extract-feature.sh"

path = sys.argv[1]
image_list = []
valid_images = [".jpg",".gif",".png"]

#for filename in glob.glob(path):
for filename in os.listdir(path):
   ext = os.path.splitext(filename)[1]
   if ext.lower() not in valid_images:
      continue
   image_list.append(os.path.join(path, filename))

#print(image_list);
#sys.exit()

model_file = './caffe-model/bvlc_reference_caffenet.caffemodel'

# I copied from: https://github.com/BVLC/caffe/blob/master/models/bvlc_reference_caffenet/deploy.prototxt
deploy_prototxt = './caffe-model/deploy.prototxt'

#Initialized the CNN
net = caffe.Net(deploy_prototxt, model_file, caffe.TEST)

#extract feature vector from the layer fc7
layer = 'fc7'
if layer not in net.blobs:
	raise TypeError("Invalid layer name: " + layer)

#Specify image mean file for the image transformer.
#I downloaded from: https://github.com/BVLC/caffe/blob/master/python/caffe/imagenet/ilsvrc_2012_mean.npy
imagemean_file ='./caffe-model/ilsvrc_2012_mean.npy'

# 
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', np.load(imagemean_file).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_raw_scale('data', 255.0)

# Reshape the network blob to the shape needed for the current CNN architecture being used
net.blobs['data'].reshape(1,3,227,227)

# load input image
for img_filename in image_list:
   print("Image filename: ", img_filename)
   
   base = os.path.splitext(img_filename)[0]
   output_file = (base + ".f") 
   print("Output filename: ", output_file)

   img = caffe.io.load_image(img_filename)
   print("Feature extraction for ", img_filename)

   #Run the image through the preprocessor:
   net.blobs['data'].data[...] = transformer.preprocess('data', img)

   #Run the image through the network
   output = net.forward()

   #Extract the feature vector from the layer of interest:
   with open(output_file, 'wb') as f:
       np.savetxt(f, net.blobs[layer].data[0], fmt='%.4f', delimiter='\n')
