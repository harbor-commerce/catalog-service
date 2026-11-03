import unittest

from app import products


class ProductsTest(unittest.TestCase):
    def test_by_id(self):
        self.assertEqual(products.by_id(2)["name"], "Notebook")

    def test_missing(self):
        self.assertIsNone(products.by_id(99))
