import numpy as np
import glob
import cv2
import os

all_data = glob.glob("temp/*.jpg")

for i in all_data:
    print(i)
    image = cv2.imread(i)
    blurred = np.hstack([cv2.blur(image, (1, 1))])

    cv2.resizeWindow('Averaged', 94, 24)

    filename = i.split("\\")[1].split(".")[0]
    cv2.imwrite("temp/"+filename + "_blur"+".jpg", blurred)