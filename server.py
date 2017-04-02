import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.web import RequestHandler
from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)


class HomePageHandler(RequestHandler):

    def get(self):
        print "GET / request from", self.request.remote_ip
        self.render("index.html")

class UserPageHandler(RequestHandler):
    def get(self):
        print "GET /user request from", self.request.remote_ip
        self.render("login.html")

class LinkTagServiceHandler(RequestHandler):
    def get(self):
        print "GET /tag request from", self.request.remote_ip
        link = self.get_argument('link','')
        # Code for classification
        tag = 'something'
        self.write({'status':'ok','tag':tag})

class LinksList(RequestHandler):
    pass


class LoginHandler(RequestHandler):

    def post(self):
        print "POST /login request from", self.request.remote_ip

        username = self.get_argument('user','')
        password = self.get_argument('pass','')
        res = db['user'].find({
            'user': username,
            'pass': password
        }).count()
        if res == 1:
            self.write({'status':'ok'})
        else:
            self.write({'status': 'not found'})


class SignUpHandler(RequestHandler):

    def post(self):
        print "POST /signup request from", self.request.remote_ip
        user_exists = db['users'].find({
            'email' : self.get_argument('email','')
        }).count()
        if user_exists == 1:
            db['users'].insert_one({
                'email': self.get_argument('email',''),
                'username': self.get_argument('user',''),
                'pass': self.get_argument('pass',''),
            })
            self.write({'status': 'ok'})
        else:
            self.write({'status': 'ok'})


handlers = [
    (r"/", HomePageHandler),
    (r"/user", UserPageHandler),
    (r"/login", LoginHandler),
    (r"/signup", SignUpHandler),
    (r"/tag", LinkTagServiceHandler),
]

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "frontend"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application(handlers, **settings)

application.listen(8000, '0.0.0.0')

tornado.ioloop.IOLoop.instance().start()
