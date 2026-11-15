import json
import unittest
from pathlib import Path


class TestSalesSummary(unittest.TestCase):

    def setUp(self):
        self.output_file = Path("summary.json")

    def load_summary(self):
        self.assertTrue(
            self.output_file.exists(),
            "summary.json is missing"
        )

        with open(self.output_file, "r") as file:
            return json.load(file)

    def test_summary_file_exists(self):
        self.assertTrue(self.output_file.exists())

    def test_valid_json(self):
        data = self.load_summary()
        self.assertIsInstance(data, dict)

    def test_regional_totals(self):
        data = self.load_summary()

        self.assertEqual(
            data["regions"],
            {
                "North": 300,
                "South": 200,
                "West": 200
            }
        )

    def test_overall_total(self):
        data = self.load_summary()
        self.assertEqual(data["overall_total"], 700)

    def test_regions_sorted(self):
        data = self.load_summary()

        self.assertEqual(
            list(data["regions"].keys()),
            ["North", "South", "West"]
        )


if __name__ == "__main__":
    unittest.main()
