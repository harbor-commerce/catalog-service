from app.products import PRODUCTS


def categories():
    return sorted({p["category"] for p in PRODUCTS})
