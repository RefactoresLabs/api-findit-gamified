class CreateItemDTO:

    """Objeto de transferência de dados para o registro de um item"""

    def __init__(
        self,
        name: str,
        description: str,
        category_id: int,
        account_id: int,
    ) -> None:

        """Inicializa os atributos de instância de CreateItemDTO

        Parameters
        ----------
        name: str
            Nome do item

        description: str
            Descrição do item

        category_id: int
            ID da categoria do item

        account_id: int
            ID da conta de usuário que registrou o item

        """

        self.__name = name
        self.__description = description
        self.__category_id = category_id
        self.__account_id = account_id

    @property
    def name(self) -> str:

        """Obtém o nome do item

        Returns
        -------
        str
            Nome do item

        """

        return self.__name

    @property
    def description(self) -> str:

        """Obtém a descrição do item

        Returns
        -------
        str
            Descrição do item

        """

        return self.__description

    @property
    def category_id(self) -> int:

        """Obtém o ID da categoria do item

        Returns
        -------
        int
            ID da categoria do item

        """

        return self.__category_id

    @property
    def account_id(self) -> int:

        """Obtém o ID da conta de usuário vinculada ao item

        Returns
        -------
        int
            ID da conta de usuário

        """

        return self.__account_id
