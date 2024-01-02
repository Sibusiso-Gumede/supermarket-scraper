"""A child class of the Supermarket base class."""

from .generic_api import BeautifulSoup, Supermarket, send_request, parse_response
from transformation import store_webpage, retrieve_webpage

class Woolworths(Supermarket):
    """The Woolworths supermarket class implementation."""
    
    def __init__(self):
        self._products_page = 'https://www.woolworths.co.za/cat/Food/'
        self._name = 'woolworths'
        self._product_categories = {
                            'Meat-Poultry-Fish': {
                                'ID': 'N-d87rb7',
                                'Products': 0
                            },
                            'Fruit-Vegetables-Salad': {
                                'ID': 'N-lllnam',
                                'Products': 0
                            },
                            'Milk-Dairy-Eggs': {
                                'ID': 'N-1sqo44p',
                                'Products': 0
                            },
                            'Ready-Meals': {
                                'ID': 'N-s2csbp',
                                'Products': 0
                            },
                            'Deli-Entertaining': {
                                'ID': 'N-13b8g51',
                                'Products': 0
                            },
                            'Food-To-Go': {
                                'ID': 'N-11buko0',
                                'Products': 0
                            },
                            'Bakery': {  
                                'ID': 'N-1bm2new',
                                'Products': 0
                            },
                            'Frozen-Food': {       
                                'ID': 'N-j8pkwq',
                                'Products': 0
                            },
                            'Pantry': {
                                'ID': 'N-1lw4dzx',
                                'Products': 0
                            },
                            'Chocolates-Sweets-Snacks': {
                                'ID': 'N-1yz1i0m',
                                'Products': 0
                            },
                            'Beverages-Juices': {
                                'ID': 'N-mnxddc',
                                'Products': 0
                            },
                            'Household': {
                                'ID': 'N-vvikef',
                                'Product': 0
                            },
                            'Cleaning': {
                                'ID': 'N-o1v4pe',
                                'Products': 0
                            },
                            'Toiletries-Health': {
                                'ID': 'N-1q1wl1r',
                                'Products': 0        
                            },
                            'Flowers-Plants': {
                                'ID': 'N-1z13rv1',
                                'Products': 0
                            },
                            'Kids': {
                                'ID': 'N-ymaf0z',
                                'Products': 0
                            },
                            'Baby': {
                                'ID': 'N-1rij75n',
                                'Products': 0
                            },
                            'Pets': {
                                'ID': 'N-l1demz',
                                'Products': 0
                            },
                            'Foodie-Gifts': {
                                'ID': 'N-18vgzb5',
                                'Products': 0
                            },    
        }
        category = list(self._product_categories.keys())[0]
        category_id = list(self._product_categories.values())[0]['ID']
        self._current_category_page = f"{self._products_page+category}/_/{category_id}"

    def get_supermarket_name(self) -> str:
        """Returns the name of the supermarket object."""
        return self._name
    
    def store_page_template(self) -> None:
        items = 2000
        complete_url = f"{self._current_category_page}/?No=120&Nrpp={items}"
        if store_webpage(send_request(complete_url), 
                                self._current_category_page):
            print("Page stored successfully.")
        else:
            print("Page not stored successfully.")
    
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

        print("Setting up supermarket attributes...")
        products = page.find('div', {'class': 'grid grid--flex grid--space-y layout--1x4'}).find_all('div', {'class': 'product-list__item'})

        for product in products:
            product_title = product.find('a', {'class': 'range--title'}).text
            product_price = product.find('strong', {'class': 'price'}).text
            product_promotion = product.find('div', {'class': 'product__price-field'}).find('a').text
            product_image_url = product.find('div', {'class': 'product--image'}).find('img').attrs['src']
            if product_promotion:
                print(f"{product_title}\n{product_price}\n{product_promotion}\n{product_image_url}\n\n")
            else:
                print(f"{product_title}\n{product_price}\n{product_image_url}\n\n")

            print("Operation complete.")    

    def get_images_path(self):
        pass

    def get_pages_path(self):
        pass           

    def get_product_image_urls(self):
        pass

    def get_current_products_page_url(self):
        return self._current_category_page