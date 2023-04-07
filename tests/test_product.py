from deal_addicts.Product import Product
from deal_addicts.ProductStatus import ProductStatus
from deal_addicts.ProductWatcher import ProductWatcher
from deal_addicts.UbiquitiWatcher import UbiquitiWatcher
import unittest

class TestProduct(unittest.TestCase):
    def test_product(self):
        products = []

        product1 = Product(1, "USW Lite 8 POE", "Ubiquiti", "usw-lite-8", 99.99, 1, True)
        products.append(product1)

        ubiquiti_watcher = UbiquitiWatcher("ca")

        for product in products:
            print("Product: ", product.product_name)
            print("Target Price: ", product.target_px)
            print("Target Quantity: ", product.target_qty)
            print("Enabled: ", product.enabled)

            if product.source == "Ubiquiti":
                status = ubiquiti_watcher.observe(product)
                print("Watcher >>> Product ID: ", status.product_id)
                print("Watcher >>> Last Px: ", status.last_px)
                print("Watcher >>> Last Qty: ", status.last_qty)
                print("Watcher >>> Last Updated: ", status.last_updated)

