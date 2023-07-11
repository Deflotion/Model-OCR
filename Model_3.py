import cv2
import matplotlib.pyplot as plt
import easyocr
import os

def ocr_plate_detection(image):
    # Mengubah gambar menjadi abu-abu
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Melakukan threshold adaptif untuk memisahkan karakter-karakter
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Mencari kontur karakter
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    plate_regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)

        # Memfilter  yang bukan plat nomor berdasarkan rasio 
        if aspect_ratio > 2 and aspect_ratio < 6:
            plate_regions.append((x, y, w, h))

    return plate_regions

def ocr_license_plate(image):
    # Menginisialisasi pembaca OCR
    reader = easyocr.Reader(['en'])

    # Melakukan OCR pada gambar
    results = reader.readtext(image)

    # Menyimpan teks koordinat
    plates = []
    coordinates = []
    for (bbox, text, _) in results:
        x, y, w, h = bbox
        plates.append(text.replace(' ', ''))
        coordinates.append((x, y, x + w, y + h))

    return plates, coordinates


# Untuk data Train
# path = r"D:/Lomba BDC/Model OCR/Data Train"
# angka_urutan = list(range(1, 801))
# angka_urutan = sorted(angka_urutan)

# for angka in angka_urutan:
#     image_name = f"DataTrain{angka}.png"
#     image_path = os.path.join(path, image_name)

#     try:
#         # Memuat gambar menggunakan OpenCV
#         image = cv2.imread(image_path)

#         # Melakukan deteksi plat nomor
#         plate_regions = ocr_plate_detection(image)

#         # Melakukan OCR pada wilayah plat nomor
#         plates, coordinates = ocr_license_plate(image)

#         # Menampilkan hasil dari model
#         print(f"Plat kendaraan dari {image_name}: {plates}")
#         print("-------------------")
#     except Exception as e:
#         print(f"Error dalam memproses {image_name}: {str(e)}")

# Untuk data test
path = r"D:/Lomba BDC/Model OCR/Data Test/"
image_name = 'DataTest90.png'
image = cv2.imread(path + image_name)
plates, coordinates = ocr_license_plate(image)

# Menampilkan hasil
print(f"Plat kendaraan dari {image_name}:{plates}")




