import web
from wechat.event_handler import IndexEventHandler
from wechat.period_retrieve_task import PeriodRetrieveTask
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

urls = (
    '/', 'IndexEventHandler'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    task = PeriodRetrieveTask()
    task.start()
    app.run()
    task.stop()
    print 'over'
else:
    import os
    import sae
    root = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(root, 'site-packages'))

    application = sae.create_wsgi_app(app.wsgifunc())

# from wechat.request import RequestParser
#
# if __name__ == "__main__":
#     with open('/home/zxy/work/code/pocket-share/src/test-data/request.xml') as r:
#         xml = r.read()
#         text_req = RequestParser.parse(xml)
#         print text_req

# from pocket.retrieve import Retrieve
#
# if __name__ == '__main__':
#     r = Retrieve()
#     print r.get_item_list()