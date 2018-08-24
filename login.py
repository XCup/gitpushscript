import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import re
from tornado.options import define,options

class loginregisterHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write()
    def post(self, *args, **kwargs):

class loginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write()
    def post(self, *args, **kwargs):

class registerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write()
    def post(self, *args, **kwargs):

if __name__=='__main__':
    app = tornado.web.Application([
        ('/',loginregisterHandler)
        ('/login',loginHandler)
        ('/register',registerHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()