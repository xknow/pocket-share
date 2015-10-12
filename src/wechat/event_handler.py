import web
import hashlib
from wechat.request import *
from pocket.retrieve import Retrieve


class IndexEventHandler(object):
    __pocket_retrieve = Retrieve()
    __TOKEN = 'crazxy'

    def GET(self):
        parameter = web.input()
        post_data = web.data()
        resp = None
        if 'echostr' in parameter:
            if self.__check_signature(parameter['signature'], parameter['timestamp'], parameter['nonce']):
                resp = parameter['echostr']
        return resp

    def POST(self):
        parameter = web.input()
        post_data = web.data()

        req = RequestParser.parse(post_data)

        return "hello"

    def __check_signature(self, signature, timestamp, nonce):
        s = ''.join([timestamp, nonce, self.__TOKEN].sort())
        return hashlib.sha1(s).hexdigest == signature
