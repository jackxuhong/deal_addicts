from enum import Enum

class ProductSource(Enum):
    UBIQUITI_CA = "UBIQUITI_CA"
    UBIQUITI_US = "UBIQUITI_US"


class Product():
    def __init__(self, product_id: int, product_name: str, source: ProductSource, product_key: str, target_px: float, target_qty: int, enabled: bool):
        self.product_id = product_id
        self.product_name = product_name
        self.source = source
        self.product_key = product_key
        self.target_px = target_px
        self.target_qty = target_qty
        self.enabled = enabled
