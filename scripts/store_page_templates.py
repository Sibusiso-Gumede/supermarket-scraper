from extraction import send_request
from supermarket_apis import Spar
from transformation import PageAsBinaryFile

def spar_page_template() -> None:
    converter = PageAsBinaryFile()
    spar = Spar()
    products_page = spar.products_page_url()
    response = send_request(products_page)
 
    if converter.store_content(response, 'Spar'):
        print("Page stored successfully.")
    else:
        print("Page not stored successfully.")

if __name__ == '__main__':
    spar_page_template()