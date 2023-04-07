from datetime import datetime
from deal_addicts.Product import Product
from deal_addicts.ProductStatus import ProductStatus
from deal_addicts.ProductWatcher import ProductWatcher


class UbiquitiWatcher(ProductWatcher):
    def __init__(self, region: str):
        self.region = region

    def get_url(self, product_key) -> str:
        if self.region == "ca":
            return "https://ca.store.ui.com/ca/en/products/" + product_key
        elif self.region == "us":
            return "https://store.ui.com/products/" + product_key
        else:
            raise Exception("Unrecognized region: " + region)


    def observe(self, product: Product) -> ProductStatus:
        url = self.get_url(product.product_key)
        print(f"Checking url {url}")
        status = ProductStatus(product.product_id, 123.22, 2, datetime.now())
        return status
