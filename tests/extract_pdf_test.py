import unittest
from extract_pdf import extract_text_from_pdf


class ExtractPdfTest(unittest.TestCase):
    def test_extract_1(self):
        pdf_path = "Landon-Hotel.pdf"
        extract_text = extract_text_from_pdf(pdf_path)

        file = open("pdf-text.txt", "w", encoding='utf-8')
        n = file.write(extract_text)
        file.close()
        self.assertTrue(n>0)


if __name__ == '__main__':
    unittest.main()
