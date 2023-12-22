from abc import ABC, abstractclassmethod

class Supermarket(ABC):
    """The base class for all supermarket classes."""

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_supermarket_name(self):
        pass

    @abstractclassmethod
    def products_page_url(self):
        pass

    @abstractclassmethod
    def get_page_increment(self):
        pass

    @abstractclassmethod
    def get_page_selectors(self):
        pass
    
    @abstractclassmethod
    def get_product_image_urls(self):
        pass

    @abstractclassmethod
    def set_product_image_urls(self):
        pass

    @abstractclassmethod
    def format_promo_description(self):
        pass
