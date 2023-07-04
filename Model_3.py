import cv2
import imutils
import easyocr
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from keras.applications.densenet import DenseNet121, preprocess_input

# Load image
path = r"D:/Lomba BDC/Model OCR/Data Test/"
image = cv2.imread(path + 'DataTest2.png')
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
    resized_image = cv2.resize(crop_image, (224, 224))  # Resize image to fixed input size

    # Load pre-trained DenseNet121 model
    base_model = DenseNet121(weights='imagenet')

    # Preprocess the image based on the model's requirements
    preprocessed_image = preprocess_input(resized_image)

    # Expand dimensions to create batch-like input
    input_image = np.expand_dims(preprocessed_image, axis=0)

    # Extract features from the image
    features = base_model.predict(input_image)

    # Flatten features and feed into OCR model
    flattened_features = features.flatten()
    readOCR = easyocr.Reader(['en'])
    result = readOCR.readtext(flattened_features)
    print(result)

# Plot contours
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.plot(location[:, 0, 0], location[:, 0, 1], 'r', linewidth=2)
plt.show()
