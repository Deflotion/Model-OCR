import os
import cv2

def deblur_image(image_path, output_path):
    # Baca gambar
    image = cv2.imread(image_path)
    
    # Konversi gambar menjadi grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Lakukan deblurring dengan metode Gaussian Blur
    deblurred = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Simpan gambar hasil deblurring
    output_filename = os.path.join(output_path, os.path.basename(image_path))
    cv2.imwrite(output_filename, deblurred)
    print(f"Gambar {image_path} telah dideblur dan disimpan di {output_filename}")

def deblur_images_in_folder(input_folder, output_folder):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List semua file dalam folder input
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Lakukan deblurring pada setiap gambar
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        deblur_image(image_path, output_folder)

if __name__ == "__main__":
    input_folder = r"D:\Lomba BDC\Model OCR\Data Test"  # Ganti dengan path folder input gambar
    output_folder = r"D:\Lomba BDC\Model OCR\Datadeblur"  # Ganti dengan path folder output
    
    deblur_images_in_folder(input_folder, output_folder)
