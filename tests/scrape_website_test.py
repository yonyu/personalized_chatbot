import unittest
from pathlib import Path
from scrape_website import scrape

target_url = "https://www.landonhotel.com"


class ExtractPdfTest(unittest.TestCase):
    def test_extract_1(self):
        scrape(target_url)
        my_file = Path('website_text.txt')
        self.assertTrue(my_file.exists())


if __name__ == '__main__':
    unittest.main()
