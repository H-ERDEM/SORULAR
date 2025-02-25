import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
#text
image = Image.open("/Users/cananerdem/Desktop/DERS/soru_4/6 56 78 90 12 34 5 9.png")
text = pytesseract.image_to_string(image)
# Çıktıyı yazdır
print("Tespit Edilen Metin:")
print(text)
#boşluk kaldırma
extracted_text = pytesseract.image_to_string(image)
numbers_list = extracted_text.split()
#sırala
number_order=sorted(numbers_list,key=int)
print(number_order)