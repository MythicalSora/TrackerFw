class Route(object):
    def __init__(self, handler, **kwargs):
        self.filters = kwargs
        self.handler = handler

    @property
    def pattern(self):
        if not 'hostname' in self.filters:
            return None

        pattern = '*://' + self.filters['hostname']

        if 'path' in self.filters:
            pattern += self.filters['path'] + '*'
        else:
            pattern += '/*'

        return pattern

    def matches(self, request):
        if 'hostname' in self.filters and \
            self.filters['hostname'] != request.host:
            return False
        elif 'path' in self.filters and \
            self.filters['path'] != request.path:
            return False

        return True