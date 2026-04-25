from datetime import date

from backend.app.domain.repositories.item_repository_interface import ItemRepositoryInterface
from backend.app.domain.entities.item import Item

from backend.app.infrastructure.persistence.models.item_model import ItemModel

from sqlalchemy.orm import Session


class ItemRepository(ItemRepositoryInterface):

    """Lida com as transações de persistência da entidade Item"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância da classe ItemRepository

        Parameters
        ----------
        session: Session
            Sessão atual que lida com as transações

        """

        self.__session = session

    def create_item(self, item: Item) -> None:

        """Cria uma nova instância na tabela item

        Parameters
        ----------
        item: Item
            Objeto da entidade item com os dados a serem armazenados

        """

        item_registry = ItemModel(
            name=item.name,
            description=item.description,
            registry_date=date.today(),
            category_id=item.category_id,
            account_id=item.account_id,
        )

        self.__session.add(item_registry)
        self.__session.flush()

    def get_all_items(self) -> list[Item]:

        """Obtém todos os itens registrados no sistema

        Returns
        -------
        list[Item]
            Lista de objetos da entidade item

        """

        item_models = self.__session.query(ItemModel).all()

        return [
            Item(
                name=model.name,
                description=model.description,
                category_id=model.category_id,
                account_id=model.account_id,
                id=model.id,
            )
            for model in item_models
        ]

    def get_item_by_id(self, id: int) -> Item | None:

        """Obtém um item pelo seu ID

        Parameters
        ----------
        id: int
            ID do item a ser buscado

        Returns
        -------
        Item | None
            Objeto da entidade item ou None se não encontrado

        """

        item_model = (
            self.__session.query(ItemModel)
            .filter(ItemModel.id == id)
            .first()
        )

        if item_model is None:
            return None

        return Item(
            name=item_model.name,
            description=item_model.description,
            category_id=item_model.category_id,
            account_id=item_model.account_id,
            id=item_model.id,
        )
