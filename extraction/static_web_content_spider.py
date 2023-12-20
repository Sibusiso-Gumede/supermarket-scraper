from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def send_request(base_address, relative_url = None) -> bytes:
    """Sends a request and returns the response in bytes."""
    if relative_url != None:
        absolute_url = urljoin(base_address, relative_url)
    else:
        absolute_url = base_address
    response = get(absolute_url)
    response.raise_for_status()
    return response.content
        
def parse_response(resp_content: bytes) -> BeautifulSoup:
    """Parses the response into a navigatable tree structure."""
    return BeautifulSoup(resp_content, 'lxml')

def download_product_image(img_absolute_url: str) -> None:
    """Sends a request to the 'assets' application of the 
    Woolworths website and stores the response."""
    # TODO: add operations to download each product image.

class WoolworthsStaticSpider():

    def capture_data(self, page: BeautifulSoup) -> None:
        """Finds and stores data that is nested within specific HTML tags."""
        
        # Find all products in the page.
        products = page.find_all('div', class_="product-list__item")
        
        # Each product has to contain: id, title, product promotion description, price and url.
        # Therefore, all of these attributes have to be present within each product element
        # object before the data can be stored in the MySQL database.
            
        for product in products:
            # Find the attributes of the product and the type of object
            # returned by the method to avoid raising TypeError exceptions:
            # if Tag object, return the text property, else return 'NoneType'.
            product_details = product.find('a', class_="range--title")
            if  self.__tag_or_none(product_details) == "<class 'NoneType'>":
                pass
            else:
                # Product ID.
                product_id = product.select_one('div[id^="prod_details"]')
                print((self.__tag_or_none(product_id, attr='id').split("_"))[-1])
                
                # Product Title.
                product_title = product_details.text
                print(product_title)

                # Product Price.
                product_price = product.find('strong', class_="price")
                print(self.__tag_or_none(product_price))
                
                # Product Promotion Description.
                product_promotion_description = product.select_one('div[class^="font-graphic"]')
                promo = self.__tag_or_none(product_promotion_description)
                

                # Product Details Page URL.
                pdp_url = urljoin(self.base_address, self.__tag_or_none(product_details, attr='href'))
                print(pdp_url) 

                product_img = product.select_one('div[class="product--image"]')
                print(product_img)

    def __tag_or_none(self, arg, attr=None) -> str:
        """Find out if the argument passed is a Tag or NoneType object.
        Returns the argument's information in string format."""

        # Return the text within the element.
        if 'Tag' in str(type(arg)):
            if attr:
                return str(arg.attrs[attr])
            else:
                return str(arg.text)
        # Return 'NoneType'.
        else:
            return str(type(arg))
        
class SparStaticSpider():

    def capture_data(self, page: BeautifulSoup) -> None:
        products = page.find('ul', {'class': 'slides', 'id': 'slideContainer'}).find_all('li')
        for product in products:
            product_image_url = product.find('a', {'data-fancybox': 'promoGal'}).attrs['href']
            print(product_image_url)