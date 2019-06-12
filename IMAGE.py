#Name:  Treeshan Yeadram
#Date:  Sept -24 -2018
#This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has only the red channel displayed.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

i =input("Enter the name of an input file: ")
out = input("Enter the name of an output file")

img = plt.imread(i) #Read in image from csBridge.png
#plt.im show(img)		           #Load image into pyplot
                        

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0    #Set the green channel to 0
img2[:,:,0] = 0    #Set the blue channel to 0


plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave(out, img2)  
