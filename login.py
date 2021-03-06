import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from asn1crypto._ffi import null
import simplejson as json

import mysqlconnectorpython
import re
from tornado.options import define,options

# class loginregisterHandler(tornado.web.RequestHandler):
#     def get(self, *args, **kwargs):
#         self.write()
#     def post(self, *args, **kwargs):

class loginHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名123
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def get(self, *args, **kwargs):
        self.write()
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        passwd = self.get_argument('passwd')
        mctp = mysqlconnectorpython
        loginresults=mctp.selectsql("select username from users where username='"+username+"' AND passwd='"+passwd+"'")
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        if(loginresults!=None):
            if(loginresults[0]!=""):
                self.write(json.dumps({'type': 0}))
                print("====>0:")
            else:
                self.write(json.dumps({'type': 1}))
                print("====>1:")
        else:
            self.write(json.dumps({'type': 1}))
            print("====>2:")
        self.finish()

class registerHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名123
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def get(self, *args, **kwargs):
        self.write()
    def post(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        username = self.get_argument('username')
        passwd = self.get_argument('passwd1')
        mctp = mysqlconnectorpython
        userresults = mctp.selectsql("select username from users where username='"+username+"'")
        print(userresults)
        if (userresults != None):
            self.write(json.dumps({'type': 1}))
            print("====>1")
        else:
            mctp.insertsql("insert into Users(username,passwd,lv) values('"+username+"','"+passwd+"',1);")
            self.write(json.dumps({'type': 0}))
            self.finish()

if __name__=='__main__':
    app = tornado.web.Application([
        #('/',loginregisterHandler)
        ('/login',loginHandler),
        ('/register',registerHandler)
    ])

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()