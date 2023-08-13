import os
import cv2

def normalize_image(image_path, output_folder):
    # Pastikan folder output ada atau buat jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Mendapatkan daftar file gambar dalam folder input
    image_files = [f for f in os.listdir(image_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # Baca gambar menggunakan OpenCV
        image = cv2.imread(os.path.join(image_path, image_file))

        if image is not None:
            # Lakukan normalisasi pada gambar (misalnya, ubah ukuran, konversi warna, dsb.)
            # Di sini Anda bisa melakukan normalisasi sesuai kebutuhan
            normalized_image = image

            # Simpan gambar yang sudah dinormalisasi di folder output
            output_file_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_file_path, normalized_image)
            print(f"Gambar {image_file} telah dinormalisasi dan disimpan di {output_folder}")

if __name__ == "__main__":
    input_folder = r"D:\Lomba BDC\Model OCR\1. Dataset\1. Data Utama\Data Train"
    output_folder = r"D:\Lomba BDC\Model OCR\1. Dataset\10. Data_Normalization\Data Train for BDC 2023 - Penyisihan"
    
    normalize_image(input_folder, output_folder)
