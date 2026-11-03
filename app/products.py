PRODUCTS = [
    {"id": 1, "name": "Mug", "price": 1990, "category": "kitchen"},
    {"id": 2, "name": "Notebook", "price": 2490, "category": "office"},
]


def by_id(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


ROUTES = {"/products": lambda: PRODUCTS}
