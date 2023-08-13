from PIL import Image
import os

def grayscale_image(input_path, output_path):
    try:
        # Membuat folder output jika belum ada
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Memeriksa setiap file di folder input
        for filename in os.listdir(input_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_file_path = os.path.join(input_path, filename)
                output_file_path = os.path.join(output_path, filename)
                
                # Membuka gambar
                img = Image.open(input_file_path)
                
                # Mengubah gambar menjadi grayscale
                grayscale_img = img.convert('L')
                
                # Menyimpan gambar grayscale
                grayscale_img.save(output_file_path)
                print(f"Grayscaled {filename} saved to {output_file_path}")

    except Exception as e:
        print("Error:", e)

# Ganti dengan path folder input dan output yang sesuai
input_folder = r'D:\Lomba BDC\Model OCR\1. Dataset\1. Data Utama\Data Train'
output_folder = r'D:\Lomba BDC\Model OCR\1. Dataset\9. Data_Grayscale\Data Train for BDC 2023 - Penyisihan'

grayscale_image(input_folder, output_folder)
