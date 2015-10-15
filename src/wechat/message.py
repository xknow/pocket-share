__author__ = 'zxy'

from xml.etree.ElementTree import *
import time

class MsgType(object):
    TEXT = 'text'
    IMAGE = 'image'


class MsgXmlElement(object):
    TO_USER_NAME = 'ToUserName'
    FROM_USER_NAME = 'FromUserName'
    CREATE_TIME = 'CreateTime'
    MSG_TYPE = 'MsgType'
    MSG_ID = 'MsgId'
    CONTENT = 'Content'


class Msg(object):
    _toUserName = ''
    _fromUserName = ''
    _createTime = ''
    _msgType = ''

    def __str__(self):
        return '\t'.join((self._toUserName, self._fromUserName, self._createTime, self._msgType))


class RequestMsg(Msg):

    _msgId = ''

    def __init__(self, xml_node):
        self._toUserName = xml_node.find(MsgXmlElement.TO_USER_NAME).text
        self._fromUserName = xml_node.find(MsgXmlElement.FROM_USER_NAME).text
        self._createTime = xml_node.find(MsgXmlElement.CREATE_TIME).text
        self._msgType = xml_node.find(MsgXmlElement.MSG_TYPE).text
        self._msgId = xml_node.find(MsgXmlElement.MSG_ID).text

    def __str__(self):
        return '\t'.join((super(RequestMsg, self).__str__(), self._msgId))

    def to_username(self):
        return self._toUserName

    def from_username(self):
        return self._fromUserName


    @staticmethod
    def create(xml_node):
        msg_type = xml_node.find(MsgXmlElement.MSG_TYPE).text
        if msg_type == MsgType.TEXT:
            return TextRequestMsg(xml_node)
        else:
            return None


class TextRequestMsg(RequestMsg):

    content = ''

    def __init__(self, xml_node):
        super(TextRequestMsg, self).__init__(xml_node)
        self.content = xml_node.find(MsgXmlElement.CONTENT).text

    def __str__(self):
        return '\t'.join((super(TextRequestMsg, self).__str__(), self.content))


class ResponseMsg(Msg):

    _template = '''
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%d</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    %s
    </xml>
    '''

    def __init__(self, to_user, from_user):
        self._toUserName = to_user
        self._fromUserName = from_user
        self._createTime = int(time.time())

    def xml(self):
        return self._template % (self._toUserName, self._fromUserName, self._createTime, self._msgType, self.subxml())

    def subxml(self):
        pass


class TextResponseMsg(ResponseMsg):

    _content = ''
    _sub_template = '<Content><![CDATA[%s]]></Content>'

    def __init__(self, to_user, from_user, content):
        super(TextResponseMsg, self).__init__(to_user, from_user)
        self._msgType = MsgType.TEXT
        self._content = content

    def subxml(self):
        return self._sub_template % self._content
