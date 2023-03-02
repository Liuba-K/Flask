from flask import Flask, render_template

from blog.views.users import users_app
from blog.views.articles import articles_app

from blog.models.database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:\\IT\\projects\\Flask\\sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")




@app.route("/")
def index():
    return render_template("index.html")


"""
@app.route("/<str:name>")
def index(name: str):
    return f"Hello {name}", 201  #предупреждение
"""


"""
#все заменить на этот код. Вариант 2
# Фабрика по созданию файлов и использованием Blueprint
from flask import Flask

from blog.user.views import user
#from blog.report.views import report

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app
    
def register_blueprints(app: Flask):
    app.register_blueprint(user)
    #app.register_blueprint(report)

"""
