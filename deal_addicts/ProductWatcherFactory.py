from deal_addicts.ProductWatcher import ProductWatcher
from deal_addicts.UbiquitiWatcher import UbiquitiWatcher


class ProductWatcherFactory():
    _watchers = {
        "UBIQUITI_CA": UbiquitiWatcher("ca"),
        "UBIQUITI_US": UbiquitiWatcher("us"),
    }

    def list_supported_sources(self):
        return self._watchers.keys()

    def get_watcher(self, source: str) -> ProductWatcher:
        watcher = self._watchers.get(source)
        if watcher == None:
            raise Exception("Unrecognized source: " + source)

        return watcher
