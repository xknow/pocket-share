__author__ = 'zxy'

from xml.etree import ElementTree
from wechat.message import RequestMsg

class RequestParser(object):

    @staticmethod
    def parse(xml):
        xml_node = ElementTree.fromstring(xml)
        return RequestMsg.create(xml_node)
