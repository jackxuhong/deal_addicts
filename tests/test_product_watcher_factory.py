from deal_addicts.ProductWatcher import ProductWatcher
from deal_addicts.ProductWatcherFactory import ProductWatcherFactory
import unittest

class TestProductWatcherFactory(unittest.TestCase):
    def test_supported_sources(self):
        factory = ProductWatcherFactory() 
        print(factory.list_supported_sources())

    def test_get_watcher(self):
        factory = ProductWatcherFactory() 
        watcher = factory.get_watcher("UBIQUITI_CA")
        print(watcher)
