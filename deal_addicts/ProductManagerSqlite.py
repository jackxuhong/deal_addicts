from deal_addicts.Product import Product
from deal_addicts.ProductManager import ProductManager
from deal_addicts.ProductStatus import ProductStatus
import sqlite3

class ProductManagerSqlite(ProductManager):
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)

    def list(self) -> list[(Product, ProductStatus)]:
        pass

    def create(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Product (product_id, product_name, source, product_key, target_px, target_qty, enabled) VALUES (?, ?, ?, ?, ?, ?, ?)", ())
        cursor.close()

    def update(self, product: Product):
        pass

    def delete(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Product WHERE product_id = ?", (product.product_id))
        cursor.close()
       
