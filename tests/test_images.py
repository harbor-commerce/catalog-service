import unittest

from app import images


class ImagesTest(unittest.TestCase):
    def test_https_only(self):
        with self.assertRaises(ValueError):
            images.set_image(1, "http://cdn/mug.png")

    def test_roundtrip(self):
        images.set_image(1, "https://cdn/mug.png")
        self.assertEqual(images.image(1), "https://cdn/mug.png")
