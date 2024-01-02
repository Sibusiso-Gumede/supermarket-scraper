# File input/output module for managing data.

from io import BytesIO
from PIL import Image, UnidentifiedImageError
from os import path, listdir, mkdir
from concurrent.futures import ThreadPoolExecutor
   
def store_webpage(content: bytes, content_name: str, path_: str) -> bool:
    """Stores the content of the response in bytes.
        Returns a true/false to confirm if the content
        is successfully stored."""
    
    if path.isdir(path_) is not True:
        mkdir(path_)
    write_bytes = BytesIO(content)
    path_ += f"/{content_name}.bin"
    with open(path_, "xb") as file:
        file.write(write_bytes.getbuffer())
    return path.isfile(path_)

def retrieve_webpage(content_name: str, path_: str) -> bytes:
    """Retrieves the stored contents of a page."""
    
    payload = bytes()
    with open(path_+f"/{content_name}.bin", "rb") as file:
        buffer_size = 2**10*8
        # Read 8kilobytes of data per cycle
        # and append it to the payload.
        buffer = file.read(buffer_size)
        while buffer:
            payload += buffer
            buffer = file.read(buffer_size)
    return payload

def store_image(img: bytes, image_name: str) -> bool:
    '''Stores byte content in image format(png, jpeg, etc).'''
    
    path_ = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{image_name.split('.')[1]}/Product Images/{image_name.split('/')[-1]}.png"
    try:
        image = Image.open(BytesIO(img))
    except UnidentifiedImageError or FileNotFoundError:
        print("Image not found or is invalid.")
    else:
        with open(path_, "xb") as file:
            image.save(file, "PNG") 
    if path.isfile(path_):    
        return True
    else:
        return False

def retrieve_image(images_dir: str):
    '''Retrieves an image file stored on disk and
        returns it in Image format.'''
    
    files = listdir(images_dir)

    if files is not None:
        # when there's more than one file in the directory
        # return a list of image file names, else return one image file
        # name.
        if len(files) > 1:
            images = list()
            for file in files:
                file = f"{images_dir}/{file}"
                images.append(Image.open(file))
            return images
        else:
            files[0] = f"{images_dir}/{files[0]}"
            return Image.open(files[0])
    elif files is None:
        raise FileNotFoundError

def resize_image(image: Image):
    '''Resizes an image.'''

    width, height = image.size
    return image.crop((width/2, 0.5, width, height))

def map_function(func, container: list):
    with ThreadPoolExecutor() as execute:
        return execute.map(func, container)