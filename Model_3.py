import cv2
import matplotlib.pyplot as plt
import easyocr

def ocr_plate_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to segment the characters
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours of characters
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    plate_regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)

        # Filter out regions that are unlikely to be license plates based on aspect ratio
        if aspect_ratio > 2 and aspect_ratio < 6:
            plate_regions.append((x, y, w, h))

    return plate_regions

def ocr_license_plate(image):
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    results = reader.readtext(image)

    # Extract the recognized text and coordinates
    plates = []
    coordinates = []
    for (bbox, text, _) in results:
        x, y, w, h = bbox
        plates.append(text.replace(' ', ''))
        coordinates.append((x, y, x + w, y + h))

    return plates, coordinates

# Path to the image
path = r"D:/Lomba BDC/Model OCR/Data Test/"
image_name = 'DataTest1.png'

# Load the image using OpenCV
image = cv2.imread(path + image_name)

# Perform license plate detection
plate_regions = ocr_plate_detection(image)

# Display the original image
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Gambar Asli')
plt.show()

# Perform OCR on the license plate regions
plates, coordinates = ocr_license_plate(image)

# Display the OCR results
for plate, (x1, y1, x2, y2) in zip(plates, coordinates):
    print("Plat Nomor:", plate)
    print("Kordinat:", (x1, y1), (x2, y2))
    print()

    # Convert coordinates to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Draw bounding box around the license plate
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the image with bounding boxes
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Deteksi pLat kendaraan')
plt.show()
