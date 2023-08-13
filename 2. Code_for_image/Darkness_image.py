from PIL import Image
import os

def darken_image(input_path, output_path, factor):
    try:
        image = Image.open(input_path)
        darkened_image = Image.eval(image, lambda x: x * factor)
        darkened_image.save(output_path)
        print(f"Image saved: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_images(input_folder, output_folder, factor):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            darken_image(input_path, output_path, factor)

if __name__ == "__main__":
    input_folder = "D:\Lomba BDC\Model OCR\Data\Data Test"  # Ganti dengan nama folder gambar input
    output_folder = "D:\Lomba BDC\Model OCR\darkened_images"  # Ganti dengan nama folder tujuan penyimpanan gambar hasil
    brightness_factor = 0.7  # Ganti faktor kecerahan sesuai kebutuhan (0.0 - 1.0)

    process_images(input_folder, output_folder, brightness_factor)
