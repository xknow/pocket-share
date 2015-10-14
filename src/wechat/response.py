__author__ = 'zxy'

from pocket.retrieve import Retrieve
from wechat.message import *

class ResponseBuilder(object):

    _requestMsg = ''

    def __init__(self, request):
        self._requestMsg = request

    def response(self):
        return RetrieverResponse(self._requestMsg).msg_str()


class Response(object):

    _requestMsg = ''

    def __init__(self, request):
        self._requestMsg = request

    def msg_str(self):
        pass


class RetrieverResponse(Response):

    def msg_str(self):
        r = Retrieve()
        items = r.get_item_list()
        content = '\n\n'.join(('\n'.join((i.resolved_title(), i.excerpt(), i.given_url())) for i in items))
        return TextResponseMsg(self._requestMsg.from_username(), self._requestMsg.to_username(), content).xml()

