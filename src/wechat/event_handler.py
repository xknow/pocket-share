import web
import hashlib
from pocket.retrieve import Retrieve


class IndexEventHandler(object):
    __pocket_retrieve = Retrieve()
    __TOKEN = 'crazxy'

    def GET(self):
        parameter = web.input()
        post_data = web.data()
        print(parameter['id'])
        print(post_data)
        return "hello"

    def __check_signature(self, signature, timestamp, nonce):
        str = ''.join([timestamp, nonce, self.__TOKEN].sort())
        return hashlib.sha1(str).hexdigest == signature
