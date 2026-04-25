from flask import request, jsonify, Flask
from dotenv import load_dotenv

import os

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.item_factories import make_item_controller
from backend.app.presentation.middlewares.jwt_required import jwt_required

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder


def create_item_routes(app: Flask) -> None:

    """Registra as rotas de item na aplicação Flask

    Parameters
    ----------
    app: Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    load_dotenv()

    @app.route("/items", methods=["POST"])
    @jwt_required
    def create_item():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ["DATABASE"],
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(body=request.get_json())

            item_controller = make_item_controller(session_manager.session)

            http_response = item_controller.handle_create(http_request)

        return jsonify(http_response.body), http_response.status_code

    @app.route("/items", methods=["GET"])
    @jwt_required
    def list_items():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ["DATABASE"],
            },
        )

        with SessionManager(database_url) as session_manager:

            item_controller = make_item_controller(session_manager.session)

            http_response = item_controller.handle_list()

        return jsonify(http_response.body), http_response.status_code
