from abc import ABC, abstractclassmethod
from requests import get
from bs4 import BeautifulSoup
import json

class Supermarket(ABC):
    """The base class for all supermarket classes."""

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_supermarket_name(self):
        pass

    @abstractclassmethod
    def get_current_products_page_url(self):
        pass
    
    @abstractclassmethod
    def get_product_image_urls(self):
        pass

    @abstractclassmethod
    def set_supermarket_attributes(self):
        pass

    @abstractclassmethod
    def store_page_template(self):
        pass

    @abstractclassmethod
    def format_promo_description(self):
        pass

    @abstractclassmethod
    def get_product_images_path(self):
        pass

    @abstractclassmethod
    def get_product_view_pages_path(self):
        pass

def send_request(url: str) -> bytes:
    """Sends a request and returns the response in bytes."""
    response = get(url)
    response.raise_for_status()
    return response.content
        
def parse_response(resp_content: bytes) -> BeautifulSoup:
    """Parses the response into a navigatable tree structure."""
    return BeautifulSoup(resp_content, 'lxml')