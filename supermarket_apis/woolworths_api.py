"""A child class of the Supermarket base class."""

from .generic_api import BeautifulSoup, Supermarket, send_request, parse_response
from transformation import store_webpage, retrieve_webpage
from time import sleep

class Woolworths(Supermarket):
    """The Woolworths supermarket class implementation."""
    
    def __init__(self):
        self.__products_page = 'https://www.woolworths.co.za/cat/Food/'
        self.__name = 'woolworths'
        self.__products_pages_path = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{self.__name}/Products_Pages"
        self.__product_view_pages_path = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{self.__name}/Product_View_Pages"
        self.__current_product_view_page_url = str()
        self.__current_product_name = str()
        self.__product_categories = {
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
        self.__current_category_name = str()
        self.__current_category_id = str()
        self.__current_category_page_url = str()
        self.__max_items_per_category = 3

    def get_supermarket_name(self) -> str:
        """Returns the name of the supermarket object."""
        return self.__name
    
    def store_page_template(self) -> None:
        complete_url = f"{self.__current_category_page_url}/?No=120&Nrpp={self.__max_items_per_category}"
        if store_webpage(send_request(complete_url), 
                        self.__current_category_page_url.split('/')[5],
                        self.__products_pages_path):
            print("Page stored successfully.")
        else:
            print("Page not stored successfully.")
    
    def store_product_view_page_template(self) -> None:
        self.__current_product_view_page_url = "https://woolworths.co.za/prod/Food/Frozen-Food/Fish-Seafood/Frozen-Mussels-with-Garlic-Herb-Butter-500-g/_/A-6009214621319?isFromPLP=true"
        self.__current_product_name = self.__current_product_view_page_url.split('/')[7]
        if store_webpage(send_request(self.__current_product_view_page_url),
                      self.__current_product_name,
                      self.__product_view_pages_path):
            print("Page successfully stored.")
        else:
            print("Page not successfully stored.")

    def scrape_items_from_category(self, page: BeautifulSoup) -> None:
        """Initializes the supermarket object attributes."""

        print("Scraping items from specified category...\n")
        products = page.find('div', {'class': 'grid grid--flex grid--space-y layout--1x4'}
                            ).find_all(
                            'div', {'class': 'product-list__item'})
        self.__product_categories[self.__current_category_name]['Products'] = list(products).__sizeof__()
        
        for product in products:
            self.__current_product_name = product.find('a', {'class': 'range--title'})
            if self.__current_product_name:
                self.__current_product_name = self.__current_product_name.text
                self.__current_product_view_page_url = product.find('a', {'class': 'range--title'}).attrs['href']            
                self.__current_product_view_page_url = f"https://www.woolworths.co.za/{self.__current_product_view_page_url}"
                
                # Retrieve image url from each product's view page.
                sleep(20)
                page = parse_response(send_request(self.__current_product_view_page_url))
                product_image = page.find('meta', {'data-react-helmet': 'true', 'property': 'og:image'}).attrs['content']                
                product_price = product.find('strong', {'class': 'price'}).text
                product_promotion = product.find('div', {'class': 'product__price-field'}).find('a')

                if product_promotion:
                    product_promotion = product_promotion.text
                    print(f"{self.__current_product_name}\n{product_price}\n{product_promotion}\n{product_image}\n\n")                
                else:
                    print(f"{self.__current_product_name}\n{product_price}\n{product_image}\n\n")
        print("\nOperation complete.")

    def scrape_items_per_category(self):
        category_names = list(self.__product_categories.keys())
        category_details = list(self.__product_categories.values())
        if category_names.__sizeof__() == category_details.__sizeof__():
        # TODO: write a loop that invokes the scrape_items_from_category function.   
            for category_name, category_detail in category_names, category_details:
                self.__current_category_name = category_name
                self.__current_category_id = category_detail['ID']
                self.__current_category_page_url = f'{self.__products_page}{self.__current_category_name}/_/{self.__current_category_id}/?No=120&Nrpp={self.__max_items_per_category}'
                self.scrape_items_from_category(parse_response(send_request(self.__current_category_page_url)))

    def get_product_images_path(self):
        pass

    def get_product_view_pages_path(self):
        return self.__product_view_pages_path           

    def get_product_image_urls(self):
        pass

    def get_current_products_page_url(self):
        return self.__current_category_page_url
    
    def get_current_category_name(self):
        return self.__current_category_name
    
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