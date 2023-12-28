"""This module extracts text from image objects."""

from pytesseract import image_to_string
from transformation import Image, retrieve_image, resize_image, map_function, listdir
from supermarket_apis import Supermarket, Spar

def product_details_ocr(supermarket: Supermarket):
    
    print(image_to_string(resize_image(Image.open(f"{supermarket.get_images_path()}/{listdir(supermarket.get_images_path())[4]}"))))
    
    #results = map_function(resize_image, images)

    #results[0].show()
    #if len(images) > 1:
    #    for image in images:
    #        print(image_to_string(image)+'\n')
    #else:
    #    print(image_to_string(images[0]))

if __name__ == '__main__':
    spar = Spar()
    product_details_ocr(spar)