from abc import ABC, abstractmethod
from deal_addicts.Product import Product
from deal_addicts.ProductStatus import ProductStatus


class ProductManager(ABC):
    
    @abstractmethod
    def list(self) -> list[Product]:
        pass
    
    @abstractmethod
    def create(self, product: Product) -> None:
        pass

    @abstractmethod
    def update(self, product: Product) -> None:
        pass

    @abstractmethod
    def delete(self, product: Product) -> None:
        pass
