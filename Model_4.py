import cv2
import imutils
import easyocr
import numpy as np
from matplotlib import pyplot as plt

# Load image
path = r"D:/Lomba BDC/Model OCR/Data Test/"
image = cv2.imread(path + 'DataTest1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Filter and find edges
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(bfilter, 30, 200)

# Find contours and sort by area
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Find the largest rectangle contour
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

print(location)

# OCR to Read Text
if location is not None:
    (x, y, w, h) = cv2.boundingRect(location)
    crop_image = gray[y:y + h, x:x + w]
    readOCR = easyocr.Reader(['en'])
    result = readOCR.readtext(crop_image)
    print(result)

    # Draw bounding box and coordinates on image
    cv2.drawContours(image, [location], -1, (0, 255, 0), 3)
    cv2.putText(image, f"({x}, {y})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Plot image with contours and coordinates
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
