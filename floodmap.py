#Name:Treeshan Yeadram
#Date:Oct 1, 2018
#This program prints floor map


import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')
mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,2] = 1.0
        elif elevations[row,col] <=6:
            floodMap[row,col,0] = 1.0
        elif elevations[row,col] <= 20:
            floodMap[row,col,0] = .5
            floodMap[row,col,1] = .5
            floodMap[row,col,2] = .5
        else:
            floodMap[row,col,1] = 1.0
            


plt.imshow(floodMap)
plt.show()
plt.imsave('floodMap.png', floodMap)
