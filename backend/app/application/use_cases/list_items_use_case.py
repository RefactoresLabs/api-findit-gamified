from backend.app.domain.repositories.item_repository_interface import ItemRepositoryInterface
from backend.app.domain.entities.item import Item


class ListItemsUseCase:

    """Caso de uso responsável pela listagem de todos os itens registrados"""

    def __init__(self, repository: ItemRepositoryInterface) -> None:

        """Inicializa os atributos de instância de ListItemsUseCase

        Parameters
        ----------
        repository: ItemRepositoryInterface
            Repositório de item para busca dos dados

        """

        self.__repository = repository

    def execute(self) -> list[Item]:

        """Executa o fluxo de listagem de todos os itens

        Returns
        -------
        list[Item]
            Lista de objetos da entidade item

        """

        return self.__repository.get_all_items()
