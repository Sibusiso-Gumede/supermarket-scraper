"""A child class of the Supermarket base class."""

from urllib.parse import urljoin
from generic_api import Supermarket

class Spar(Supermarket):
	"""The Spar supermarket class implementation."""

	def __init__(self):
		self.base_address = 'https://www.spar.co.za'
		self.name = 'Spar'
		self.page_selectors = {
			'product_list': 'ul[class="slides"] > li[style^="width"]',
			'product_id': '',
			'product_title': '',
			'product_price': '',
			'product_promo': '',
			'product_img': 'div[class="item-image"] > img[width="168px"]',
		}		
		self.page_increment = 1

	def get_supermarket_name(self) -> str:
		"""Returns the name of the supermarket object."""
		return self.name
	
	def products_page_url(self, page_number=0) -> str:
		"""Returns the absolute url of a webpage."""
		return urljoin(self.base_address, f'/Specials')
	
	def get_page_increment(self) -> int:
		"""Returns the page increment of the website."""
		return self.page_increment
	
	def get_page_selectors(self) -> dict[str]:
		"""Returns a dictionary of CSS selectors."""
		return self.page_selectors
	
	def format_promo_description(self) -> str or None:
		"""Returns a formatted promotion description of the product."""
		return None