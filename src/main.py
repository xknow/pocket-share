import web
from wechat.event_handler import IndexEventHandler

urls = (
    '/', 'IndexEventHandler'
)

if __name__ == "__main__":
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")

    l = ['1', '2', '3sdf']
    print ''.join(l)
    l.sort()
    sum = reduce(lambda x, y: x + y, l)
    print sum
    app = web.application(urls, globals())
    app.run()
