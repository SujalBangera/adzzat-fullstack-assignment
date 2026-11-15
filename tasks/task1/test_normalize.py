
import unittest
from tag_utils import normalize_tag


class TestNormalizeTag(unittest.TestCase):

    def test_basic_text(self):
        self.assertEqual(
            normalize_tag("Python Programming"),
            "python-programming"
        )

    def test_remove_extra_spaces(self):
        self.assertEqual(
            normalize_tag("  Hello   World  "),
            "hello-world"
        )

    def test_remove_punctuation(self):
        self.assertEqual(
            normalize_tag("Web Development!"),
            "web-development"
        )

    def test_uppercase_text(self):
        self.assertEqual(
            normalize_tag("HELLO WORLD"),
            "hello-world"
        )

    def test_empty_string(self):
        self.assertEqual(normalize_tag(""), "")

    def test_numbers(self):
        self.assertEqual(
            normalize_tag("Python 3 Programming"),
            "python-3-programming"
        )
    def test_multiple_punctuation_marks(self):
        self.assertEqual(
            normalize_tag("Data, Science: AI!"),
            "data-science-ai"
        )

if __name__ == "__main__":
    unittest.main()
