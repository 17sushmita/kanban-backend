from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] \
        = os.environ['DATABASE_URL']

    from app.database.sqlalchemy_extension import db

    db.init_app(app)

    from app.api.api_extension import api

    api.init_app(app)

    return app


application = create_app()


@application.before_first_request
def create_tables():
    from app.database.sqlalchemy_extension import db

    db.create_all()


if __name__ == "__main__":
    application.run(port=5000, debug=True)
