class Sniffer(object):
    """ A auto-updated web spider """
    def __init__(self):
        self.name = 'as you wish'
        self.domain = 'crawl frontier'
        # is the resource is continue updating?
        self.updating = False
        # how many days dose this resource update once?
        self.update_cycle = 0

    def register(self, aggregation):
        self.aggregation = aggregation

    def search_book(self, query):
        pass

    def update(self):
        # build or update Resource
        pass
