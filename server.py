import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.web import RequestHandler
from pymongo import MongoClient

client = MongoClient('localhost', 27017)


class HomePageHandler(RequestHandler):

    def get(self):
        print "GET / request from", self.request.remote_ip
        self.render("index.html")

class UserPageHandler(RequestHandler):
    def get(self):
        print "GET /user request from", self.request.remote_ip
        self.render("index.html")

class LoginHandler(RequestHandler):

    def post(self):
        print "POST /login request from", self.request.remote_ip

        username = self.get_argument('user','')
        password = self.get_argument('pass','')
        res = db['boats'].find({
            'phone': phone,
            'password': password
        }).count()
        if res == 1:
            self.write({'status':'ok'})
        self.write({'status': 'ok'})


class SignUpHandler(RequestHandler):

    def post(self):
        print "POST /signup request from", self.request.remote_ip
        self.write({'status': 'ok'})


handlers = [
    (r"/", HomePageHandler),
    (r"/user", UserPageHandler),
    (r"/login", LoginHandler),
    (r"/signup", SignUpHandler),
]

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application(handlers, **settings)

application.listen(8000, '0.0.0.0')

tornado.ioloop.IOLoop.instance().start()
