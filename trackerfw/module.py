class Module(object):
    def routes():
        raise Exception('please override `routes`')

    async def handler(request):
        raise Exception('please override `handler`')