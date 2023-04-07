from abc import ABC, abstractmethod
from deal_addicts.Product import Product
from deal_addicts.ProductStatus import ProductStatus

class ProductWatcher(ABC):
    @abstractmethod
    def get_url(self, product_key: str) -> str:
        pass


    @abstractmethod
    def observe(self, product: Product) -> ProductStatus:
        pass
