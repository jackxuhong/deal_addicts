from datetime import datetime

class ProductStatus:
    def __init__(self):
        pass

    def __init__(self, product_id: int, last_px: float, last_qty: int, last_updated: datetime):
        self.product_id = product_id
        self.last_px = last_px
        self.last_qty = last_qty
        self.last_updated = last_updated

    