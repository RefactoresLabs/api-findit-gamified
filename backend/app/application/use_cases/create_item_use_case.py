from backend.app.domain.repositories.item_repository_interface import ItemRepositoryInterface
from backend.app.domain.entities.item import Item

from backend.app.application.dtos.create_item_dto import CreateItemDTO


class CreateItemUseCase:

    """Caso de uso responsável pelo registro de um novo item"""

    def __init__(self, repository: ItemRepositoryInterface) -> None:

        """Inicializa os atributos de instância de CreateItemUseCase

        Parameters
        ----------
        repository: ItemRepositoryInterface
            Repositório de item para persistência dos dados

        """

        self.__repository = repository

    def execute(self, dto: CreateItemDTO) -> None:

        """Executa o fluxo de registro de um novo item

        Parameters
        ----------
        dto: CreateItemDTO
            Objeto de transferência de dados com as informações do item

        """

        item = Item(
            name=dto.name,
            description=dto.description,
            category_id=dto.category_id,
            account_id=dto.account_id,
        )

        self.__repository.create_item(item)
