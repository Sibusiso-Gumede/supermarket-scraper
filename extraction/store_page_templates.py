from supermarket_apis import (Supermarket, Spar, Woolworths,
                            PicknPay, Shoprite, Checkers, send_request)
from transformation import store_webpage

def supermarket_page_template(supermarket: Supermarket) -> None:
    supermarket = Supermarket()
    products_page = supermarket.products_page_url()
 
    if store_webpage(send_request(products_page), 
                            supermarket.products_page_url(), "web page"):
        print("Page stored successfully.")
    else:
        print("Page not stored successfully.")


if __name__ == '__main__':
    woolies = Woolworths()
    supermarket_page_template(woolies)