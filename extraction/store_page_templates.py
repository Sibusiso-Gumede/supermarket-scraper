from extraction import send_request
from supermarket_apis import (Supermarket, Spar, Woolworths,
                            PicknPay, Shoprite, Checkers)
from transformation import ContentAsBinaryFile

def supermarket_page_template(supermarket: Supermarket) -> None:
    supermarket = Supermarket()
    products_page = supermarket.products_page_url()
 
    if ContentAsBinaryFile.store_content(send_request(products_page), 
                            supermarket.products_page_url(), "web page"):
        print("Page stored successfully.")
    else:
        print("Page not stored successfully.")


if __name__ == '__main__':
    woolies = Woolworths()
    supermarket_page_template(woolies)