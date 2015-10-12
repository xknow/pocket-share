__author__ = 'zxy'


class ResponseBuilder(object):

    _request = ''

    def __init__(self, request):
        self._request = request

    def response(self):
        pass



class Response(object):

    def toXml(self):
        pass

