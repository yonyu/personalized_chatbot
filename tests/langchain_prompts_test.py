import unittest
from langchain_prompts import run_prompts


class LangchainPromptsTest(unittest.TestCase):
    """
    run the test case, in the test console to start the conversation:
    you: hit
    chatGPT: Hello! Welcome to Landon Hotel. How may I assist you?
    you: what's your name?
    chatGPT: My name is Mr. Landon, and I am the hotel manager of Landon Hotel in London's West End. How may I assist you?
    you: what time to check in
    chatGPT: Check-in time at Landon Hotel is at 3:00 pm. If you need to check in earlier, please let us know and we will do our best to accommodate your request.
    click on 'Stop' to end the conversation
    """
    @staticmethod
    def test_prompts():
        run_prompts()
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
