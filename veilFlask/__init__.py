import os
from flask import Flask

# chrome://net-internals/#sockets

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # Todo: This should be something secret when the app is real. It's fine as DEV for now
        SECRET_KEY='dev',
        # Learn more about this in later sections
        DATABASE=os.path.join(app.instance_path, 'veilFlask.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #  Add the command-line command to Flask "init-db"
    # run "flask --app veilFlask init-db" to create the instance flaskr.sqlite
    from . import db
    db.init_app(app)


    from . import auth
    app.register_blueprint(auth.bp)

    from . import characterReporting as cR
    app.register_blueprint(cR.bp)



    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app