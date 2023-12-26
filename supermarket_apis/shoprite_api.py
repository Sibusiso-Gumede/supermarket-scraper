"""A child class of the Supermarket base class."""

from .generic_api import Supermarket, BeautifulSoup, urljoin

class Shoprite(Supermarket):
	"""The Shoprite supermarket class implementation."""

	def __init__(self):
		self.base_address = 'https://www.shoprite.co.za'
		self.name = 'shoprite'
		self.page_selectors = {
			'product_list': '',
			'product_id': '',
			'product_title': '',
			'product_price': '',
			'product_promo': '',
			'product_img': '',
		}		
		self.page_increment = 1

	def get_supermarket_name(self) -> str:
		"""Returns the name of the supermarket object."""
		return self.name
	
	def products_page_url(self, page_number=0) -> str:
		"""Returns the absolute url of a webpage."""
		return urljoin(self.base_address, f'')
	
	def get_page_increment(self) -> int:
		"""Returns the page increment of the website."""
		return self.page_increment
	
	def get_page_selectors(self) -> dict[str]:
		"""Returns a dictionary of CSS selectors."""
		return self.page_selectors
