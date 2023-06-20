from playwright.sync_api import sync_playwright, expect, Route
from woolworths_plugin import Woolworths
from supermarket_interface import Supermarket

def handle_route(route: Route) -> None:
    """Modifies the response header,
    'content-type': 'text/html'."""

    response = route.fetch()
    body = response.text()
    body = body.replace("<title>", "<title>Modified Response")
    route.fulfill(
        response=response,
        body=body,
        headers={**response.headers, "content-type": "text/html"},
    )

def capture_data(sm_websites: list[Supermarket]) -> None:

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        
        page = context.new_page()
        # Abort image loading.
        page.route("**/*.{png,jpg,jpeg,svg}", lambda route: route.abort())
        #page.route("**/*", handle_route)
        
        for sm_website in sm_websites:
            # Capture the product data from the list of websites.
            page_number = 0
            page_increment = sm_website.get_page_increment()
            # Navigate through all the available products promotion pages.
            # The main page of the promoted products.
            page.goto(sm_website.products_page_url())
            while True:
                if page_number > 0:
                    # Proceed to the next page.
                    response = page.goto(sm_website.products_page_url(page_number=page_number))
                
                if response.status != 404:
                    break

                # Get page selectors.
                list_selector = sm_website.get_page_selectors()['product_list']
                id_selector = sm_website.get_page_selectors()['product_id']
                title_selector = sm_website.get_page_selectors()['product_title']
                price_selector = sm_website.get_page_selectors()['product_price']
                promo_selector = sm_website.get_page_selectors()['product_promo']
                image_selector = sm_website.get_page_selectors()['product_img']

                product_list = page.query_selector_all(list_selector)
                for product in product_list:
                    print((product.query_selector(id_selector).get_attribute('id')).split('_')[-1])
                    print(product.query_selector(title_selector).text_content())
                    print(product.query_selector(price_selector).text_content())
                    print(product.query_selector(promo_selector).text_content())
                    print(product.query_selector(image_selector).get_attribute('src'))
                page_number += page_increment

        context.close()
        browser.close()

if __name__ == "__main__":
    woolworths = Woolworths()
    websites = [
        woolworths,
    ]
    capture_data(websites)