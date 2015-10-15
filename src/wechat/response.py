# coding=utf-8

__author__ = 'zxy'

from wechat.message import *
from wechat.period_retrieve_task import PeriodRetrieveTask


class ResponseBuilder(object):

    _requestMsg = ''

    def __init__(self, request):
        self._requestMsg = request

    def response(self):
        return RetrieverResponse(self._requestMsg).msg_str()


class Response(object):

    _instructions = "输入格式：年月日，例如20151010，获取所输入时间对应的文章列表"
    _requestMsg = ''

    def __init__(self, request):
        self._requestMsg = request

    def msg_str(self):
        pass


class RetrieverResponse(Response):

    def msg_str(self):
        if not isinstance(self._requestMsg, TextRequestMsg):
            return TextResponseMsg(self._requestMsg.from_username(), self._requestMsg.to_username(), self._instructions).xml()

        if PeriodRetrieveTask.all_items is None:
            return TextResponseMsg(self._requestMsg.from_username(),self._requestMsg.to_username(), "正在同步，请稍后发送请求").xml()

        t = self._requestMsg.content
        try:
            req_time = time.mktime(time.strptime(t, '%Y%m%d'))
        except Exception, e:
            req_time = 0
        if req_time == 0:
            content = self._instructions
        else:
            items = [i for i in PeriodRetrieveTask.all_items
                     if i.time_added() > req_time and i.time_added() - req_time <= 24*3600]
            content = '\n\n'.join(('\n'.join((i.resolved_title(), i.excerpt(), i.given_url())) for i in items))
        return TextResponseMsg(self._requestMsg.from_username(), self._requestMsg.to_username(), content).xml()

