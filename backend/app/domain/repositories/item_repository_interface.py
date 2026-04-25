from abc import ABC, abstractmethod

from backend.app.domain.entities.item import Item


class ItemRepositoryInterface(ABC):

    """Interface para persistência da entidade Item"""

    @abstractmethod
    def create_item(self, item: Item) -> None:

        """Persiste um novo item no banco de dados

        Parameters
        ----------
        item: Item
            Objeto da entidade item com os dados a serem armazenados

        """

    @abstractmethod
    def get_all_items(self) -> list[Item]:

        """Obtém todos os itens registrados no sistema

        Returns
        -------
        list[Item]
            Lista de objetos da entidade item

        """

    @abstractmethod
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
