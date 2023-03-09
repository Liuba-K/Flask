from blog.app import app

from blog.models.database import db
#from blog.app import db, create_app
#app = create_app()

@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")

@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="admin", is_staff=True)
    james = User(username="james")#, email='dfsf@email.com', password=generate_password_hash('test123'))
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        #port=5010,
    )


"""
#вариант 2
from blog.app import create_app

app = create_app()
"""