
import uuid
from typing import Optional, List

# from typing import  List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import get_by_id, get_many, save


def product_create(id: str, name: str, price: float):
    product = (Product(id, name, price))
    save(product)
    return {"success": True, "product": product}

def product_get_by_id(id:str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)

























