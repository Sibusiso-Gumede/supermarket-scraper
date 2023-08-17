"""This module extracts text from image objects."""

from pytesseract import pytesseract
#from PIL import Image
import file_io

# The PIL image module is already included in the file_io module
# so therefore we don't need to explicitly import it on this
# module.

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
images_path = r"C:\Users\Acer\Documents\dev_env\discount_my_groceries\website_api's\product_images\spar_products"

images = file_io.BinaryContentAsImage.retrieve_image(images_path)
pytesseract.tesseract_cmd = tesseract_path

if len(images) > 1:
    for image in images:
        print(pytesseract.image_to_string(image)+'\n')
else:
    print(pytesseract.image_to_string(images[0]))
