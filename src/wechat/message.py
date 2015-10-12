__author__ = 'zxy'


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

    def __init__(self):
        pass

    def __init__(self, to_user, from_user, create_time, msg_type, msg_id):
        self._toUserName = to_user
        self._fromUserName = from_user
        self._createTime = create_time
        self._msgType = msg_type

    def __init__(self, xml_node):
        self._toUserName = xml_node.find(MsgXmlElement.TO_USER_NAME).text
        self._fromUserName = xml_node.find(MsgXmlElement.FROM_USER_NAME).text
        self._createTime = xml_node.find(MsgXmlElement.CREATE_TIME).text
        self._msgType = xml_node.find(MsgXmlElement.MSG_TYPE).text

    def __str__(self):
        return '\t'.join((self._toUserName, self._fromUserName, self._createTime, self._msgType))


class RequestMsg(Msg):

    _msgId = ''

    def __init__(self, xml_node):
        super(RequestMsg, self).__init__(xml_node)
        self._msgId = xml_node.find(MsgXmlElement.MSG_ID).text

    def __str__(self):
        return '\t'.join((super(RequestMsg, self).__str__(), self._msgId))

    @staticmethod
    def create(xml_node):
        msg_type = xml_node.find(MsgXmlElement.MSG_TYPE).text
        if msg_type == MsgType.TEXT:
            return TextRequestMsg(xml_node)
        else:
            return None


class TextRequestMsg(RequestMsg):

    _content = ''

    def __init__(self, xml_node):
        super(TextRequestMsg, self).__init__(xml_node)
        self._content = xml_node.find(MsgXmlElement.CONTENT).text

    def __str__(self):
        return '\t'.join((super(TextRequestMsg, self).__str__(), self._content))
