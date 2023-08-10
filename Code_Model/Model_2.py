import os
import re
import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ASUS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Untuk Train
# folder_path = 'Data Train'
# angka_urutan = list(range(1,801))
# angka_urutan = sorted(angka_urutan)

# for angka in angka_urutan:
#     filename = f"DataTrain{angka}.png"
#     img_path = os.path.join(folder_path, filename)

#     if os.path.isfile(img_path):
#         img = cv2.imread(img_path)
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
#         pil_img = Image.fromarray(img_rgb)
#         extracted_text = pytesseract.image_to_string(pil_img)
#         # Menghapus spasi dari hasil ekstraksi teks
#         extracted_text = extracted_text.replace(" ", "")
#         print(f"File: {filename}")
#         print(extracted_text)
#         print("-------------------------")  

# Untuk Test
folder_path = 'Data Test'

filename = f"DataTest90.png"
img_path = os.path.join(folder_path, filename)

if os.path.isfile(img_path):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    pil_img = Image.fromarray(img_rgb)
    extracted_text = pytesseract.image_to_string(pil_img)
    # Menghapus spasi dari hasil ekstraksi teks
    extracted_text = extracted_text.replace(" ", "")
    print(f"File: {filename}")
    print(extracted_text)
    print("-------------------------")  