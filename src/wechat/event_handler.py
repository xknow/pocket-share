import web
import hashlib
from wechat.request import *
from wechat.response import *
from pocket.retrieve import Retrieve


class IndexEventHandler(object):
    __pocket_retrieve = Retrieve()
    __TOKEN = 'crazxy'

    def GET(self):
        parameter = web.input()
        post_data = web.data()
        resp = None
        if 'echostr' in parameter:
            if self.__check_signature(parameter.get('signature', 's'), parameter.get('timestamp', 't'), parameter.get('nonce', 'n')):
                resp = parameter['echostr']
        return resp

    def POST(self):
        parameter = web.input()
        post_data = web.data()

        req = RequestParser.parse(post_data)
        resp = RetrieverResponse(req)

        return resp.msg_str()

    def __check_signature(self, signature, timestamp, nonce):
        l = [timestamp, nonce, self.__TOKEN]
        l.sort()
        s = ''.join(l)
        return hashlib.sha1(s).hexdigest == signature
