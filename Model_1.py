import cv2
import imutils
import easyocr
import numpy as np
from matplotlib import pyplot as plt
import os

# Untuk Train
# path = r"D:/Lomba BDC/Model OCR/Data Train"
# folder_path = 'Data Train'
# angka_urutan = list(range(1, 801))
# angka_urutan = sorted(angka_urutan)

# for angka in angka_urutan:
#     nama_file = f"DataTrain{angka}.png"
#     image_path = os.path.join(path, nama_file)
#     image = cv2.imread(image_path)
    
#     try:
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#         # Filter dan find edged
#         bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
#         edged = cv2.Canny(bfilter, 30, 200)

#         # Mencari contour berdasarkan daerah
#         contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         contours = imutils.grab_contours(contours)
#         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

#         # Cari contour terbesar
#         location = None
#         for contour in contours:
#             approx = cv2.approxPolyDP(contour, 10, True)
#             if len(approx) == 4:
#                 location = approx
#                 break

#         # Membaca dan menampilkan hasil
#         print(f"hasil {nama_file}:")
#         if location is not None:
#             (x, y, w, h) = cv2.boundingRect(location)
#             crop_image = gray[y:y + h, x:x + w]
#             readOCR = easyocr.Reader(['en'])
#             result = readOCR.readtext(crop_image)
#             print(result)
#         else:
#             print("Tidak dapat menemukan lokasi teks.")
#         print("-------------------")
#     except Exception as e:
#         print(f"Error dalam memproses {nama_file}: {str(e)}")


# Untuk test
path = r"D:/Lomba BDC/Model OCR/Data Test/"
nama_file = 'DataTest90.png'
image = cv2.imread(path + nama_file)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Filter dan find edges
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(bfilter, 30, 200)

# Mencari contours berdasarkan area
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Mencari contour terbesar
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

# print(location)

# Membaca OCR dan menampilkan hasil
print(f"hasil {nama_file}:")
if location is not None:
    (x, y, w, h) = cv2.boundingRect(location)
    crop_image = gray[y:y + h, x:x + w]
    readOCR = easyocr.Reader(['en'])
    result = readOCR.readtext(crop_image)
    print(result)
    print("-------------------")
# Plot contours
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.plot(location[:, 0, 0], location[:, 0, 1], 'r', linewidth=2)
# plt.show()




