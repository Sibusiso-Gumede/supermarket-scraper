"""A child class of the Supermarket base class."""

from .generic_api import BeautifulSoup, Supermarket, urljoin

class Woolworths(Supermarket):
    """The Woolworths supermarket class implementation."""
    
    def __init__(self):
        self.base_address = 'https://www.woolworths.co.za'
        self.name = 'woolworths'
        self.page_increment = 24
        self.categories = {
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
        self.product_count_per_category = dict()

    def get_supermarket_name(self) -> str:
        """Returns the name of the supermarket object."""
        return self.name
    
    def products_page_url(self, total_items) -> str:
        """Returns the absolute url of a webpage."""
        return urljoin(self.base_address, f'/cat/Food/_/N-1z13sk5Zxtznwk?No=24&Nrpp={total_items}')
    
    def get_page_increment(self) -> int:
        """Returns the page increment of the website."""
        return self.page_increment
    
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
            product_title = product.find('a', {'class': 'range--title'}).text
            product_price = product.find('strong', {'class': 'price'}).text
            product_promotion = product.find('div', {'class': 'product__price-field'}).find('a').text
            product_image_url = product.find('div', {'class': 'product--image'}).find('img').attrs['src']
            if product_promotion:
                print(f"{product_title}\n{product_price}\n{product_promotion}\n{product_image_url}\n\n")
            else:
                print(f"{product_title}\n{product_price}\n{product_image_url}\n\n")
            