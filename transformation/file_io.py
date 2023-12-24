# File input/output module for managing data.

from io import BytesIO
from PIL import Image, UnidentifiedImageError
from os import path, listdir

class PageAsBinaryFile():
    """A class for storing and retrieving HTML pages in binary format."""
        
    def store_content(content: bytes, supermarket_name, product_title=None, page_type='products', page_number=0) -> bool:
        """Stores the contents of the page in bytes.
            Returns a true/false to confirm if the page
            is successfully stored."""
        try:
            assert page_number >= 0
        except AssertionError:
            print("Invalid page number")
        else:
            write_bytes = BytesIO(content)
            
            if page_type == 'products' and product_title == None:
                path_ =  f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_templates/{supermarket_name}_templates/page_{page_number}.bin"
            elif page_type == 'product_display_page' and product_title != None:
                path_ = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_templates/{supermarket_name}_templates/{product_title}_page.bin"
            with open(path_, "xb") as file:
                file.write(write_bytes.getbuffer())
            return path.isfile(path_)

    def retrieve_content(supermarket_name, product_title=None, page_type='products', page_number=0) -> bytes:
        """Retrieves the stored contents of a page."""
        try:
            assert page_number >= 0
        except AssertionError:
            print("Invalid argument value.")
        else:
            payload = bytes()
            path_ = str()
            if page_type == 'products' and product_title == None:
                path_ = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{supermarket_name}/Pages/page_{page_number}.bin"        
            elif page_type == 'product_display_page' and product_title != None:
                path_ = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{supermarket_name}/Pages/{product_title}_page.bin"
            with open(path_, "rb") as file:
                buffer_size = 2**10*8
                # Read 8kilobytes of data per cycle
                # and append it to the payload.
                buffer = file.read(buffer_size)
                while buffer:
                    payload += buffer
                    buffer = file.read(buffer_size)
            return payload

class BinaryContentAsImage():

    def store_image(img: bytes, image_name: str) -> str:
        '''Stores byte content in image format.'''
        
        try:
            image = Image.open(BytesIO(img))
        except UnidentifiedImageError or FileNotFoundError:
            print("Image not found or is invalid.")
        else:
            # The image name consists of a url. 
            # Therefore, we retrieve the name of the supermarket from the base address.
            with open(f'/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{image_name.split(".")[1]}/Product Images/{image_name}', "xb") as file:
                image.save(file, "JPEG") 
                return(f"{image_name} successfully saved.")

    def retrieve_image(files_dir: str):
        '''Retrieves an image file stored in binary format and
           returns it in Image format.'''
        
        files = listdir(files_dir)

        if files is not None:
            # when there's more than one file in the directory
            # return a list of image file names, else return one image file
            # name.
            if len(files) > 1:
                images = []
                for file in files:
                    file = f"{files_dir}/{file}"
                    images.append(Image.open(file))
                return images
            else:
                files[0] = f"{files_dir}/{files[0]}"
                return Image.open(files[0])
        elif files is None:
            raise FileNotFoundError
