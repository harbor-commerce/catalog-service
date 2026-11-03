IMAGES = {}


def set_image(product_id, url):
    if not url.startswith("https://"):
        raise ValueError("images must be https")
    IMAGES[product_id] = url


def image(product_id):
    return IMAGES.get(product_id)
