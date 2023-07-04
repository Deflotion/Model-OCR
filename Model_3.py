import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import imutils
from imutils import paths

# Fungsi untuk mendeteksi plat kendaraan menggunakan EasyOCR
def detect_plates(image):
    # Mengubah gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Menerapkan teknik pengurangan noise dan deteksi tepi
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    # Mencari kontur pada gambar tepi
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    plates = []

    # Melakukan loop pada kontur yang dideteksi
    for contour in contours:
        # Menghitung area kontur
        area = cv2.contourArea(contour)

        # Mengecek apakah area kontur memenuhi batasan tertentu
        if area > 500:
            # Mendapatkan koordinat dan ukuran bounding box
            (x, y, w, h) = cv2.boundingRect(contour)

            # Mengekstrak region of interest (ROI)
            roi = image[y:y + h, x:x + w]

            # Menambahkan ROI ke daftar plat kendaraan yang dideteksi
            plates.append(roi)

    return plates

# Path gambar
path = r"D:/Lomba BDC/Model OCR/Data Test/"
image_path = path + 'DataTest2.png'

# Membaca gambar plat kendaraan
image = cv2.imread(image_path)

# Menginisialisasi model EasyOCR
reader = easyocr.Reader(['en'], gpu=False)

# Mendeteksi plat kendaraan
plates = detect_plates(image)

# Melakukan OCR pada setiap plat kendaraan
for plate in plates:
    # Menggunakan EasyOCR untuk mendapatkan teks dari plat
    results = reader.readtext(plate)

    # Menampilkan hasil OCR dan koordinat pada gambar
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(plate, cv2.COLOR_BGR2RGB))

    for (bbox, text, _) in results:
        # Menghapus spasi dari teks
        text = text.replace(' ', '')

        # Mendapatkan koordinat bounding box
        x = bbox[0][0]
        y = bbox[0][1]
        width = bbox[1][0] - bbox[0][0]
        height = bbox[1][1] - bbox[0][1]

        # Menampilkan teks pada gambar
        ax.text(x, y, text, fontsize=10, color='red')

        # Menampilkan bounding box pada gambar
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='red', facecolor='none')
        ax.add_patch(rect)

    plt.show()
