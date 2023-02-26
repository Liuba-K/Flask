from flask import Blueprint, render_template

articles_app = Blueprint("articles_app", __name__)
ARTICLES = ["Flask", "Django", "JSON:API"]


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    try:
        article_title = ARTICLES[article_id]
    except KeyError:
        raise NotFound("Article  doesn't exist")
    return render_template('articles/details.html', article_id=article_id, article_title=article_title)
