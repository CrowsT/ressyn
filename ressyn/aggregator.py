class Aggregator(object):
    def __init__(self, config):
        self.config = config

        self.handlers = {
            "search book": self.search_book,
            "get catalogue": self.get_catalogue,
            "get section": self.get_section,
            "get book": self.get_book,
        }

    def search_book(self, content):
        pass

    def get_catalogue(self, content):
        pass

    def get_section(self, content):
        pass

    def get_book(self, content):
        pass

    def request_handler(self, request):
        pass