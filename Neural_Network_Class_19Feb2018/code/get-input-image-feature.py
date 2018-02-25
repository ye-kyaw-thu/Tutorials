import sys
import cv2
import numpy as np
import caffe
import glob
import os, os.path

input_image_file = sys.argv[1]

valid_images = [".jpg",".gif",".png"]

ext = os.path.splitext(input_image_file)[1]
if ext.lower() in valid_images:
   model_file = '/home/lar/experiment/obj-recog2/10obj/caffe-model/bvlc_reference_caffenet.caffemodel'

   # I copied from: https://github.com/BVLC/caffe/blob/master/models/bvlc_reference_caffenet/deploy.prototxt
   deploy_prototxt = '/home/lar/experiment/obj-recog2/10obj/deploy/deploy.prototxt'

   #Initialized the CNN
   net = caffe.Net(deploy_prototxt, model_file, caffe.TEST)

   #extract feature vector from the layer fc7
   layer = 'fc7'
   if layer not in net.blobs:
      raise TypeError("Invalid layer name: " + layer)

   #Specify image mean file for the image transformer.
   #I downloaded from: https://github.com/BVLC/caffe/blob/master/python/caffe/imagenet/ilsvrc_2012_mean.npy
   imagemean_file ='/home/lar/experiment/obj-recog2/10obj/deploy/ilsvrc_2012_mean.npy'
 
   transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
   transformer.set_mean('data', np.load(imagemean_file).mean(1).mean(1))
   transformer.set_transpose('data', (2,0,1))
   transformer.set_raw_scale('data', 255.0)

   # Reshape the network blob to the shape needed for the current CNN architecture being used
   net.blobs['data'].reshape(1,3,227,227)

   # load input image
   base = os.path.splitext(input_image_file)[0]
   output_file = (base + ".f") 
   print("Output filename: ", output_file)

   img = caffe.io.load_image(input_image_file)
   print("Feature extraction for ", input_image_file)

   #Run the image through the preprocessor:
   net.blobs['data'].data[...] = transformer.preprocess('data', img)

   #Run the image through the network
   output = net.forward()

   #Extract the feature vector from the layer of interest:
   with open(output_file, 'wb') as f:
      np.savetxt(f, net.blobs[layer].data[0], fmt='%.4f', delimiter='\n')
else:
   print("Error: Input file extension should be .jpg, .gif or .png!")
   exit()


