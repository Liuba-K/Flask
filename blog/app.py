from blog.security import flask_bcrypt
from flask import Flask, render_template
from flask_migrate import Migrate

from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import login_manager, auth_app
from blog.views.authors import authors_app

from blog.models.database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:\\IT\\projects\\Flask\\sqlite.db"
#/home/PycharmProjects/Flask/blog/
#from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(app)
#
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = "abcdefg123456"
app.config["WTF_CSRF_ENABLED"] = True  # по умолчанию


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")

migrate = Migrate(app, db, compare_type=True)
login_manager.init_app(app)
db.init_app(app)
flask_bcrypt.init_app(app)

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
@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
