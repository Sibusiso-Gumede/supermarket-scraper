"""A child class of the Supermarket base class."""

from urllib.parse import urljoin
from generic_api import Supermarket

class Woolworths(Supermarket):
    """The Woolworths supermarket class implementation."""
    
    def __init__(self):
        self.base_address = 'https://www.woolworths.co.za'
        self.name = 'Woolworths'
        self.page_selectors = {
            'product_list': 'div.product-list__item',
            'product_id': 'div[id^="prod_details"]',
            'product_title': 'div[class^="product"] > div[class^="range"] > a',
            'alt_product_title': 'h2[itemprop="name"]',
            'product_price': 'strong.price',
            'product_promo': 'div[class^="font-graphic"] > a[href^="/cat"] > div',
            'product_img': 'div[class="product--image"] > img',
        }
        self.page_increment = 24
        self.product_count_per_category = dict()

    def get_supermarket_name(self) -> str:
        """Returns the name of the supermarket object."""
        return self.name
    
    def products_page_url(self) -> str:
        """Returns the absolute url of a webpage."""
        return urljoin(self.base_address, f'/cat/Food/_/N-1z13sk5Zxtznwk?No=24&Nrpp={total_items}')
    
    def get_page_increment(self) -> int:
        """Returns the page increment of the website."""
        return self.page_increment
    
    def get_page_selectors(self) -> dict[str]:
        """Returns a dictionary of CSS selectors."""
        return self.page_selectors
    
    def format_promo_description(self, promo: str):
        """Sorts the product promotion description into a list.
        
           First string is the WRewards promotion and the second
           is the general promotion."""
        
        # Check if the promotion description has the WRewards promotion.
        if 'eward' in promo:
            promotions = []
            counter = 0

            while True:
                # Make use of ASCII values to distinguish the alphabets in an efficient manner.
                current_letter = ord(promo[counter])
                next_letter = ord(promo[counter+1])
                if (((96 < current_letter) and (current_letter < 123)) or 
                    ((64 < current_letter) and (current_letter < 91))) and (next_letter == 66):
                    # B = 66 'Buy' is on the right. Therefore, append WRewards first to the list.
                    promotions.append(promo[:counter])
                    promotions.append(promo[counter+1:])
                    break
                elif (((96 < current_letter) and (current_letter < 123)) or 
                    ((64 < current_letter) and (current_letter < 91))) and (next_letter == 87):
                    # W = 87 'WRewards' is on the right. Therefore, append WRewards first to the list.
                    promotions.append(promo[counter+1:])
                    promotions.append(promo[:counter])
                    break
                # Return the original text if the discount description only has a WREWARDS deal.
                elif (counter == (len(promo)-1)):
                    promotions.append(promo)
                    break
                counter += 1
            
            return promotions
        else:
            return promo

    def set_supermarket_attributes(self, page: BeautifulSoup) -> None:
        """Initializes the supermarket object attributes."""
        products = page.find('div', {'class': 'grid grid--flex grid--space-y layout--1x4'}).find_all('div', {'class': 'product-list__item'})
        
        for product in products:
