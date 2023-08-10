import os
import numpy as np
import cv2

# Path ke folder gambar input
input_folder = r"D:\Model-OCR-main\Model-OCR-main\Data Test"
# Path ke folder tujuan untuk gambar yang sudah di-sharpen
output_folder = r"D:\Model-OCR-main\Model-OCR-main\datasharpening"

# Membuat folder tujuan jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Mendapatkan daftar nama file gambar dalam folder input
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Loop melalui setiap file gambar
for image_file in image_files:
    # Membaca gambar menggunakan OpenCV
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)
    
    img = cv2.imread(input_path)
    
    # Menentukan kernel sharpening
    kernel = [[-1, -1, -1],
              [-1,  9, -1],
              [-1, -1, -1]]
    kernel = np.array(kernel)
    
    # Melakukan konvolusi dengan kernel sharpening
    sharpened_img = cv2.filter2D(img, -1, kernel)
    
    # Menyimpan gambar yang sudah di-sharpen
    cv2.imwrite(output_path, sharpened_img)

print("Sharpening selesai dan gambar disimpan dalam folder tujuan.")
