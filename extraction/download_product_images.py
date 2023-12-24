#from playwright.async_api import async_playwright
from concurrent.futures import ThreadPoolExecutor
from extraction import parse_response
from transformation import BinaryContentAsImage, PageAsBinaryFile
from supermarket_apis import Supermarket, Spar
import requests
#import asyncio

class DownloadDynamically():

    async def get_product_image_urls(sm: Supermarket, page):

            image_urls = []
            prod_list_selector = sm.get_page_selectors()['product_list']       
            image_selector = sm.get_page_selectors()['product_img']
            product_list = await page.query_selector_all(prod_list_selector)

            for product in product_list:
                image_element = await product.query_selector(image_selector)
                if image_element is not None:
                    image_urls.append(f"www.{sm.get_supermarket_name()}.co.za{await image_element.get_attribute('src')})")
            sm.set_product_image_urls(image_urls)

    async def screenshot_product_images(sm: Supermarket, page) -> None:

        product_slides = len(await page.query_selector_all('div[class="flex-viewport"] > ul[class="slides"] > li[style^="width"]'))
        count = 1
        type = "jpeg"
        path = r"/home/workstation33/Documents/dev_env/discount_my_groceries/website_api's/product_images/spar_products"
        quality = 100
        properties = {type, path, quality}
        while count <= product_slides:
            if count == 1:
                await page.locator(".wrapper > a").first.click()
            elif 1 < count <= product_slides:
                await page.locator("#fancybox-container-1").press("ArrowRight")
            await page.screenshot(path=path+f"/product{count}.jpeg")
            count += 1             
                       
class DownloadStatically():
    def download_and_store(sm: Supermarket):
        # verify if there are product image urls provided with the object.
        # if so, proceed to download and store them.
        try: 
            assert sm.get_product_image_urls() is not None
        except AssertionError:
            print("No image urls were provided.")
        else:
            with ThreadPoolExecutor() as exec:
                print(exec.map(download_image, sm.get_product_image_urls()))                      

async def execute_browser(operation: str, sm: Supermarket):
    async with async_playwright() as pw:
            
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        response = await page.goto(sm.products_page_url(), timeout=120000)
        assert response.status != 404

        if operation == 'get_product_image_urls':
            DownloadDynamically.get_product_image_urls(sm, page)
        else:
            DownloadDynamically.screenshot_product_images(sm, page)

def download_image(image_link: str) -> None:
    response =  requests.get(image_link).content
    return BinaryContentAsImage.store_image(response, image_link)

if __name__ == "__main__":
    supermarket = Spar()
    supermarket.set_product_details(parse_response(PageAsBinaryFile.retrieve_content(supermarket.name)))
    DownloadStatically.download_and_store(supermarket)
    #asyncio.run(execute_browser())