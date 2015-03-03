import tornado.ioloop
import tornado.web
import tornado.gen
import time
from tornado-asynctool import AsyncUtils

_ASYNC = AsyncUtils(5) #set threading pool size 5

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(“Hello, world”)

class MainAsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        res = yield _ASYNC.cmd(time.sleep,10) #sleep 10s
        self.write(“Hello, world2″)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/async", MainAsyncHandler),
])

if __name__ == “__main__”:
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

