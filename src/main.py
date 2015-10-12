import web
from wechat.event_handler import IndexEventHandler

urls = (
    '/', 'IndexEventHandler'
)

# if __name__ == "__main__":
#     import sys
#
#     reload(sys)
#     sys.setdefaultencoding("utf-8")
#
#     print True
#     app = web.application(urls, globals())
#     app.run()


from wechat.request import RequestParser

if __name__ == "__main__":
    with open('/home/zxy/work/code/pocket-share/src/test-data/request.xml') as r:
        xml = r.read()
        text_req = RequestParser.parse(xml)
        print text_req