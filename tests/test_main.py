import unittest

import main


class TestMain(unittest.TestCase):
    def test_get_message(self) -> None:
        self.assertEqual(main.get_message(), "aasa")


if __name__ == "__main__":
    unittest.main()
