from flask import Flask

from backend.app.presentation.routers.user_account_routes import create_user_account_routes

def create_app() -> Flask:

    """Cria a interface da aplicação entre o cliente e servidor, com as respectivas rotas

    Returns
    -------
    Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    app = Flask(__name__)

    create_user_account_routes(app) # Rotas das contas de usuários

    return app