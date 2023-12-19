from extraction import send_request
from supermarket_apis import Spar
from transformation import PageAsBinaryFile

def spar_page_template(template_buffer: PageAsBinaryFile) -> None:
    spar = Spar()
    try:
        assert template_buffer.store_content(send_request(spar.products_page_url()),
                                spar.get_supermarket_name())
    except AssertionError:
        print("Page not stored successfully.")
    else:
        print("Page stored successfully.")

if __name__ == '__main__':
    buffer = PageAsBinaryFile()
    spar_page_template(buffer)