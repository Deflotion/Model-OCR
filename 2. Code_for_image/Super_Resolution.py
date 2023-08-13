import os
import cv2
from PIL import Image

def super_resolve_image(input_path, output_path, scale_factor):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_path, filename)
            output_image_path = os.path.join(output_path, filename)

            # Load image using OpenCV
            img = cv2.imread(input_image_path)

            # Perform super-resolution using OpenCV's resize function
            height, width, _ = img.shape
            new_height = height * scale_factor
            new_width = width * scale_factor
            resized_img = cv2.resize(img, (int(new_width), int(new_height)), interpolation=cv2.INTER_CUBIC)

            # Save the super-resolved image using PIL
            pil_image = Image.fromarray(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
            pil_image.save(output_image_path)

            print(f"Processed: {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    input_folder = r"D:\Lomba BDC\Model OCR\Data Test"  # Ganti dengan path folder input
    output_folder = r"D:\Lomba BDC\Model OCR\Datasuperresolusi"  # Ganti dengan path folder output
    scale_factor = 2  # Ganti sesuai dengan faktor skalasi yang diinginkan
    
    super_resolve_image(input_folder, output_folder, scale_factor)
