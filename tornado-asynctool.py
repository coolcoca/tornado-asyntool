from concurrent.futures import ThreadPoolExecutor
from tornado.ioloop import IOLoop
from tornado.concurrent import run_on_executor

class AsyncUtils:
    def __init__(self,num_worker=10):
        self.io_loop = IOLoop.current()
        self.executor = ThreadPoolExecutor(num_worker)

    @run_on_executor
    def cmd(self,func, *args, **kwargs):
        res = func(*args,**kwargs)
        return res
