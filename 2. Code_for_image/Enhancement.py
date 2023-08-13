import os
import cv2

# Fungsi untuk mengaplikasikan filter pada gambar
def apply_filters(image):
    # Contoh: Menggunakan filter Gaussian Blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred

# Path folder input dan output
input_folder = r"D:\Lomba BDC\Model OCR\1. Dataset\1. Data Utama\Data Train"
output_folder = r"D:\Lomba BDC\Model OCR\1. Dataset\7. Data_Image_Enhancement_Filters\Data Train for BDC 2023 - Penyisihan"

# Membuat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop melalui setiap gambar di folder input
for image_name in os.listdir(input_folder):
    if image_name.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, image_name)

        # Baca gambar
        image = cv2.imread(image_path)

        if image is not None:
            # Aplikasikan filter
            enhanced_image = apply_filters(image)

            # Simpan gambar hasil filter ke folder output
            cv2.imwrite(output_path, enhanced_image)

            print(f"Image {image_name} processed and saved.")

print("Image enhancement process complete.")