from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.create_item_dto import CreateItemDTO
from backend.app.application.use_cases.create_item_use_case import CreateItemUseCase
from backend.app.application.use_cases.list_items_use_case import ListItemsUseCase


class ItemController:

    """Ponto de acesso entre os endpoints de item e os casos de uso correspondentes"""

    def __init__(
        self,
        create_item_use_case: CreateItemUseCase,
        list_items_use_case: ListItemsUseCase,
    ) -> None:

        """Inicializa os atributos de instância de ItemController

        Parameters
        ----------
        create_item_use_case: CreateItemUseCase
            Caso de uso de registro de item

        list_items_use_case: ListItemsUseCase
            Caso de uso de listagem de itens

        """

        self.__create_item_use_case = create_item_use_case
        self.__list_items_use_case = list_items_use_case

    def handle_create(self, http_request: HttpRequest) -> HttpResponse:

        """Registra um novo item com os dados obtidos do endpoint

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint

        Returns
        -------
        HttpResponse
            Resposta HTTP com status de criação ou erro

        """

        body = http_request.body

        required_fields = ["name", "description", "category_id", "account_id"]

        if not all([field in body.keys() for field in required_fields]):
            return HttpResponse(
                400,
                {"message": "Campos obrigatórios não informados"},
            )

        for field in ["name", "description"]:
            if isinstance(body[field], str) and not body[field].strip():
                return HttpResponse(
                    400,
                    {"message": f"Campo {field} está vazio"},
                )

        dto = CreateItemDTO(
            name=body["name"],
            description=body["description"],
            category_id=body["category_id"],
            account_id=body["account_id"],
        )

        self.__create_item_use_case.execute(dto)

        return HttpResponse(
            201,
            {"message": "Item registrado com sucesso!"},
        )

    def handle_list(self) -> HttpResponse:

        """Retorna todos os itens registrados no sistema

        Returns
        -------
        HttpResponse
            Resposta HTTP com a lista de itens

        """

        items = self.__list_items_use_case.execute()

        items_data = [
            {
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "category_id": item.category_id,
                "account_id": item.account_id,
            }
            for item in items
        ]

        return HttpResponse(200, {"items": items_data})
