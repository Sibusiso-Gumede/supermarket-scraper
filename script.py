from playwright.sync_api import Playwright, sync_playwright, expect
from woolworths_plugin import Woolworths

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.woolworths.co.za/cat/Food/_/N-1z13sk5Zxtznwk?No=120&Nrpp=60")
    page.wait_for_timeout(10000)

    woolworths = Woolworths()
    products = page.query_selector_all(woolworths.get_page_selectors()['product_list'])
    if len(products) > 0:
        print('products found.')
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)