__author__ = 'zxy'

from wechat.message import RequestMsg
from xml.etree import ElementTree

class RequestParser(object):

    @staticmethod
    def parse(xml):
        xml_node = ElementTree.fromstring(xml)
        return RequestMsg.create(xml_node)
