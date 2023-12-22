#from playwright.async_api import async_playwright
from concurrent.futures import ThreadPoolExecutor
from transformation import BinaryContentAsImage
from supermarket_apis import Supermarket
from supermarket_apis import Spar
import asyncio
import requests

class Dynamic():
    async def scrape_urls(self, page, sm: Supermarket):
        """Captures image urls from a website using a website's selectors
            and returns the urls in a list."""
        
        image_urls = []
        prod_list_selector = sm.get_page_selectors()['product_list']       
        image_selector = sm.get_page_selectors()['product_img']
        product_list = await page.query_selector_all(prod_list_selector)

        for product in product_list:
            image_element = await product.query_selector(image_selector)
            if image_element is not None:
                image_urls.append("https://www.spar.co.za"+(await image_element.get_attribute('src')))
        return image_urls

    async def screenshot_images(self, page):
        """Screenshots product images and stores them in a directory."""

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

def download_image(image_link: str):
    response =  requests.get(image_link).content
    BinaryContentAsImage.store_image(response, image_link.split('/')[-2])

if __name__ == "__main__":
    spar = Spar()

    async def get_product_images():
        async with async_playwright() as pw:
            dyna = Dynamic()
            browser = await pw.chromium.launch(headless=False)
            context = await browser.new_context()
            page = await context.new_page()
            response = await page.goto(spar.products_page_url(), timeout=120000)
            assert response.status != 404
            #await scrape_urls(page, spar)
            await dyna.screenshot_images(page)

    #asyncio.run(get_product_images())
                    
