from PIL import Image
import os

# Path ke folder input dan output
input_folder = r"D:\Lomba BDC\Model OCR\1. Dataset\1. Data Utama\Data Train"
output_folder = r"D:\Lomba BDC\Model OCR\1. Dataset\8. Data_RGB\Data Train for BDC 2023 - Penyisihan"

# Fungsi untuk memanipulasi gambar (contoh: invert warna)
def manipulate_image(image_path):
    image = Image.open(image_path)
    manipulated_image = Image.eval(image, lambda px: 255 - px)  # Invert warna
    return manipulated_image

# Memastikan folder output sudah ada atau dibuat
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Mengambil daftar file dalam folder input
image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg") or f.endswith(".png")]

# Loop melalui setiap file gambar dalam folder input
for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)
    
    # Memanipulasi gambar
    manipulated_image = manipulate_image(input_path)
    
    # Menyimpan gambar hasil manipulasi ke folder output
    manipulated_image.save(output_path)
    
    print(f"Gambar {image_file} telah dimanipulasi dan disimpan di {output_path}")
