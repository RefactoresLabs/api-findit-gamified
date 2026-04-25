from backend.app.application.use_cases.create_item_use_case import CreateItemUseCase
from backend.app.application.use_cases.list_items_use_case import ListItemsUseCase

from backend.app.infrastructure.persistence.repositories.item_repository import ItemRepository

from backend.app.presentation.controllers.item_controller import ItemController

from sqlalchemy.orm import Session


def make_item_controller(session: Session) -> ItemController:

    """Factory function que cria um objeto ItemController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    ItemController
        Ponto de acesso dos endpoints de item

    """

    item_repository = ItemRepository(session)

    create_item_use_case = CreateItemUseCase(item_repository)
    list_items_use_case = ListItemsUseCase(item_repository)

    return ItemController(create_item_use_case, list_items_use_case)
