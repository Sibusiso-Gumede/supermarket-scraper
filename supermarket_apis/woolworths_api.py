"""A child class of the Supermarket base class."""

from .generic_api import BeautifulSoup, Supermarket, send_request, parse_response
from transformation import store_webpage, retrieve_webpage, map_function, store_image
from time import sleep

class Woolworths(Supermarket):
    """The Woolworths supermarket class implementation."""
    
    def __init__(self):
        self.__products_page = 'https://www.woolworths.co.za/cat/Food/'
        self.__name = 'woolworths'
        self.__category_pages_path = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{self.__name}/category_pages"
        self.__product_view_pages_path = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{self.__name}/product_view_pages"
        self.__product_images_path = f"/home/workstation33/Documents/Development Environment/Projects/discount_my_groceries/dmg_django/supermarket_resources/{self.__name}/product_images"
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
        self.__category_page_urls = list()

    def get_supermarket_name(self) -> str:
        """Returns the name of the supermarket object."""
        return self.__name
    
    def store_page_template(self) -> None:
        complete_url = f"{self.__current_category_page_url}/?No=120&Nrpp={self.__max_items_per_category}"
        if store_webpage(send_request(complete_url), 
                        self.__current_category_page_url.split('/')[5],
                        self.__category_pages_path):
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

    def __scrape_items_from_category(self, category_url: str) -> None:
        page = parse_response(send_request(category_url))
        category_products_view_page_urls = list()        
        products = page.find('div', {'class': 'grid grid--flex grid--space-y layout--1x4'}
                            ).find_all(
                            'div', {'class': 'product-list__item'})
        self.__product_categories[self.__current_category_name]['Products'] = list(products).__sizeof__()
        for product in products:
            self.__current_product_name = product.find('a', {'class': 'range--title'})
            if self.__current_product_name:
                self.__current_product_name = self.__current_product_name.text
                self.__current_product_view_page_url = product.find('a', {'class': 'range--title'}).attrs['href']
                category_products_view_page_urls.append(f"https://www.woolworths.co.za/{self.__current_product_view_page_url}")                
                product_price = product.find('strong', {'class': 'price'}).text
                product_promotion = product.find('div', {'class': 'product__price-field'}).find('a')
        
                if product_promotion:
                    product_promotion = product_promotion.text
                    print(f"{self.__current_product_name}\n{product_price}\n{product_promotion}\n{product_image}\n\n")                
                else:
                    print(f"{self.__current_product_name}\n{product_price}\n{product_image}\n\n")
        sleep(10)
        results = map_function(self.__download_and_store_product_image, category_products_view_page_urls)
        for result in results:
            if result == False:
                print("Product images were not successfully stored.")
                return
        print("\nOperation successfully complete.")

    def scrape_items(self):
        category_names = list(self.__product_categories.keys())
        category_details = list(self.__product_categories.values())
        if category_names.__sizeof__() == category_details.__sizeof__(): 
            for (category_name, category_detail) in zip(category_names, category_details):
                self.__current_category_name = category_name
                self.__current_category_id = category_detail['ID']
                sleep(10)
                self.__scrape_items_from_category(f'{self.__products_page}{self.__current_category_name}/_/{self.__current_category_id}/?No=120&Nrpp={self.__max_items_per_category}')

    def __download_and_store_product_image(self, url):
        # Retrieve image url from each product's view page.
        page = parse_response(send_request(url))
        product_image_url = page.find('meta', {'data-react-helmet': 'true', 'property': 'og:image'}).attrs['content']
        sleep(10)
        store_image(send_request(product_image_url), self.__name, url.split('/')[-3], self.__current_category_name)

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