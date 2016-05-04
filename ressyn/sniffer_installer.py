class SnifferInstaller(object):
    def __init__(self, config):
        self.config = config
        self.handlers = {
            "sniffer install": self.install,
            "sniffer update": self.update,
            "sniffer list": self.list,
            "sniffer uninstall": self.uninstall,
        }

    def install(self, content):
        pass

    def update(self, content):
        pass

    def list(self, content):
        pass

    def uninstall(self, content):
        pass

    def request_handler(self, request):
        pass