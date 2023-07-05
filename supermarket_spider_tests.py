from woolworths_api import Woolworths
from file_io import PageAsBinaryFile
from unittest import TestCase, TextTestRunner, TestSuite

class SupermarketSpiderTestCase(TestCase):
    """Test cases for the supermarket spiders."""
    def test_spider():
        # To be written...

def suite():
    suite = TestSuite()
    suite.addTest(SupermarketSpiderTestCase('test_spider'))
    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(suite())
        
