from PIL import Image
import os

input_folder = r'D:\Lomba BDC\Model OCR\Data Test'  # Ganti dengan path folder input Anda
output_folder = r'D:\Lomba BDC\Model OCR\Datahitamputih'  # Ganti dengan path folder output Anda

# Pastikan folder output ada atau buat jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List semua file dalam folder input
input_files = os.listdir(input_folder)

for file_name in input_files:
    if file_name.endswith(('.png', '.jpg', '.jpeg')):  # Filter hanya file gambar
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        
        # Buka gambar menggunakan PIL
        image = Image.open(input_path)
        
        # Konversi ke hitam putih (grayscale)
        grayscale_image = image.convert("L")
        
        # Simpan gambar ke folder output
        grayscale_image.save(output_path)
        
        print(f"Gambar {file_name} berhasil diubah menjadi hitam putih dan disimpan di {output_path}")
