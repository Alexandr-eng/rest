
import uuid
from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import get_by_id, get_many, save


def product_create(id: str, name: str, price: float) -> Product:
    product = Product(id, name, price)
    save(product)
    return product


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)
























