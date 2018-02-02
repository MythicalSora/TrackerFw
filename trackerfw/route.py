class Route(object):
    def __init__(self, handler, **kwargs):
        self.filters = kwargs
        self.handler = handler

    def matches(self, request):
        if 'hostname' in self.filters and \
            self.filters['hostname'] != request.host:
            return False
        elif 'path' in self.filters and \
            self.filters['path'] != request.path:
            return False

        return True