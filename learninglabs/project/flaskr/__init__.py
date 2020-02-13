import os 

from flask import Flask

def create_app(test_config=None):
    #criando e configurando o app 

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else: 
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    #Conexão com o DB
    from . import db
    db.init_app(app)

    return app 

    #Registro / Autenticação 
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app 
    
    #Rodando o app
    @app.route('/')
    @app.route('/hello')

    def hello():
        return 'Hello World!'
    
    return app