import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector


path = "Face-image-dataset-small"
images = []
ages = []

detector = FaceDetector()

for img in os.listdir(path):
    try:
        print(img)
        if img!='.git':
            age = img.split("_")[0]
            ages.append(age)
            img = cv2.imread(str(path)+"/"+str(img))
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            
            # Detect the face in the image and store the result in img, bbox variables
            
 
            # if bbox exits then
            
                # Get the X,Y,W,H of bbox in respective variables i.e X, Y, W, H
                

                # Crop the face out of the image
                
                # Resize the image to 200, 200
                        
                # Append resized image to images array  

                
    except:
        print("error in reading")

ages = np.array(ages,dtype=np.int64)

# Convert images to np.array

print("Age",ages)

# Print images array
