import os
import cv2

# Fungsi untuk melakukan denoising pada gambar
def denoise_image(input_path, output_path):
    image = cv2.imread(input_path)
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)  # Menyesuaikan parameter sesuai kebutuhan
    cv2.imwrite(output_path, denoised_image)

# Folder input dan output
input_folder = r"D:\Lomba BDC\Model OCR\Data Test"
output_folder = r"D:\Lomba BDC\Model OCR\Denoising"

# Membuat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop melalui setiap file gambar dalam folder input
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Sesuaikan dengan format gambar yang Anda miliki
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        denoise_image(input_path, output_path)
        print(f"Processed: {filename}")

print("Denoising selesai!")
