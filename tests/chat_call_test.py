import unittest
from chat_call import call_chat


class ChatCallTest(unittest.TestCase):
    def test_extract_1(self):
        content = call_chat()
        self.assertTrue(len(content) > 0)


if __name__ == '__main__':
    unittest.main()