import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.web import RequestHandler
from pymongo import MongoClient
import os
from analysis.LinkClassifier import LinkClassifier

client = MongoClient('localhost', 27017)
db = client['mlhprime']

# link_classifier = LinkClassifier()


class BaseHandler(RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie('user')


class HomePageHandler(BaseHandler):

    def get(self):
        print 'GET / request from', self.request.remote_ip
        if not self.current_user:
            self.redirect('/login')
            return
        user = tornado.escape.xhtml_escape(self.current_user)
        self.render("index.html", user=user)


class LinkTagServiceHandler(RequestHandler):

    def get(self):
        print 'GET /tag request from', self.request.remote_ip
        link = self.get_argument('link', '')
        tag = link_classifier.classify_link(link)
        self.write({'status': 'ok', 'tag': tag})


class LinksList(RequestHandler):
    pass


class LoginHandler(RequestHandler):

    def get(self):
        print 'GET /login request from', self.request.remote_ip
        self.render('login.html')

    def post(self):
        print 'POST /login request from', self.request.remote_ip

        email = self.get_argument('email', '')
        password = self.get_argument('pass', '')

        res = db['user'].find({
            'email': email,
            'pass': password
        }).count()
        if res == 1:
            self.set_secure_cookie('user', username)
            self.redirect('/')
        else:
            pass


class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie('user')
        self.redirect('/')


class SignUpHandler(RequestHandler):

    def post(self):
        print 'POST /signup request from', self.request.remote_ip
        user_exists = db['users'].find({
            'email': self.get_argument('email', '')
        }).count()
        if user_exists == 1:
            db['users'].insert_one({
                'email': self.get_argument('email', ''),
                'username': self.get_argument('user', ''),
                'pass': self.get_argument('pass', ''),
            })
            self.set_secure_cookie('user', username)
            self.redirect('/')
        else:
            self.write({'status': 0, 'message': 'already registered'})


handlers = [
    (r"/", HomePageHandler),
    # (r"/user", UserPageHandler),
    (r"/login", LoginHandler),
    (r"/signup", SignUpHandler),
    (r"/logout", LogoutHandler),
    (r"/tag", LinkTagServiceHandler),
    (r"/assets/(.*)", tornado.web.StaticFileHandler,
     {"path": os.path.join(os.path.dirname(__file__), "frontend/assets")}),
    (r"/bower_components/(.*)", tornado.web.StaticFileHandler,
     {"path": os.path.join(os.path.dirname(__file__), "frontend/bower_components")}),
]

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "frontend"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    login_url="/login",
)

application = tornado.web.Application(handlers, **settings)
print 'Server is running...'
application.listen(8000, '0.0.0.0')

tornado.ioloop.IOLoop.instance().start()
