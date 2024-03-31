import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector

path = "Face-image-dataset-small"

detector = FaceDetector()

for img in os.listdir(path):
    try:
        print(img)

        # Check if img is not equal to .git i.e a wrong format image 
        
            # Get the age from the image path i.e img

            #Append age to ages array
            
            # Read the image
            
            # Convert image from BGR to RGB format
            

            # Display the age on the image
            
    except:
        print("error in reading")

# Convert ages to np.array

# Print ages
