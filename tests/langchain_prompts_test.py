import unittest
from langchain_prompts import run_prompts


class LangchainPromptsTest(unittest.TestCase):
    def test_prompts(self):
        run_prompts()
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
