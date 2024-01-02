from supermarket_apis import Woolworths, parse_response
from transformation import retrieve_webpage

if __name__ == '__main__':
    woolies = Woolworths()
    woolies.set_supermarket_attributes(parse_response(retrieve_webpage(woolies.get_current_products_page_url())))
    #woolies.store_page_template()