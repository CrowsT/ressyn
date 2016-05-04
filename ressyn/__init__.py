from .sniffer_installer import SnifferInstaller
from .aggregator import Aggregator
from . import response


class Ressyn(object):
    def __init__(self, config):
        self.config = config
        self.sniffer_installer = SnifferInstaller(config)
        self.aggregator = Aggregator(config)

        self.handlers = {
            "sniffer": self.sniffer_installer.request_handler,

            "default": self.aggregator.request_handler,
        }

    def request_handler(self, request):
        if "request" in request:
            method = request["request"].split()[0]
            if method in self.handlers:
                handler = self.handlers[method]
            else:
                handler = self.handlers["default"]
            return handler(request)
        else:
            return response.fail("Unknown request method")