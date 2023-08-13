import os
import cv2

def contrast_enhancement(image):
    # Melakukan peningkatan kontras pada gambar
    alpha = 1.5  # Faktor kontras
    beta = 30    # Peningkatan kecerahan
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return enhanced_image

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)
        
        image = cv2.imread(input_path)
        if image is not None:
            enhanced_image = contrast_enhancement(image)
            cv2.imwrite(output_path, enhanced_image)
            print(f"Processed: {image_file}")
        else:
            print(f"Error reading: {image_file}")

if __name__ == "__main__":
    input_folder = r"D:\Lomba BDC\Model OCR\Datasharpening2"  # Ganti dengan path folder gambar input
    output_folder = r"D:\Lomba BDC\Model OCR\Data_Contrast_Enhancement_sharp"  # Ganti dengan path folder tujuan output
    process_images(input_folder, output_folder)
