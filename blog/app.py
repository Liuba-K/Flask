from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app

app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")

"""
@app.route("/<str:name>")
def index(name: str):
    return f"Hello {name}", 201  #предупреждение
"""


@app.route("/")
def index():
    return render_template("index.html")

"""
#все заменить на этот код. Вариант 2
# Фабрика по созданию файлов и использованием Blueprint
from flask import Flask

from blog.user.views import user
#from blog.report.views import report

def create_app() -> Flask:
    app = Flask(__name)
    register_blueprints(app)
    return app
    
def register_blueprints(app: Flask):
    app.register_blueprint(user)
    #app.register_blueprint(report)
"""
