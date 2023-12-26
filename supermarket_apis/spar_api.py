"""A child class of the Supermarket base class."""

from .generic_api import Supermarket, BeautifulSoup, urljoin

class Spar(Supermarket):
	"""The Spar supermarket class implementation."""

	def __init__(self):
		self.base_address = 'https://www.spar.co.za'
		self.name = 'spar'	
		self.page_increment = 1
		self.product_image_urls = []

	def get_supermarket_name(self) -> str:
		"""Returns the name of the supermarket object."""
		return self.name
	
	def products_page_url(self, page_number=0) -> str:
		"""Returns the absolute url of a webpage."""
		return urljoin(self.base_address, f'/Specials')
	
	def get_page_increment(self) -> int:
		"""Returns the page increment of the website."""
		return self.page_increment
	
	def get_product_image_urls(self) -> list:
		"""Returns a list of product image urls."""
		return self.product_image_urls
	
	def set_supermarket_attributes(self, page: BeautifulSoup):
		"""Initializes the supermarket object attributes."""
		products = page.find('ul', {'class': 'slides', 'id': 'slideContainer'}).find_all('li')
		for product in products:
			#self.product_image_urls.append(self.base_address+product.find('a', {'data-fancybox': 'promoGal'}).attrs['href'])
			image_url = product.find('div', {'class': 'item-image'})
			if image_url != None:
				self.product_image_urls.append(f"{self.base_address+image_url.find('img').attrs['src']}")

	def format_promo_description(self) -> str or None:
		"""Returns a formatted promotion description of a product."""
		return None
