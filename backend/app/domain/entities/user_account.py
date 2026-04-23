class UserAccount:

    """Representa a entidade conta de usuário da regra de negócio"""

    def __init__(self, name: str, email: str, password: str, phone: str) -> None:

        """Inicializa os atributos de instância de UserAccount

        Parameters
        ----------
        name: str
            Nome completo do usuário
        
        email: str
            E-mail do usuário
        
        password: str
            Senha do usuário
        
        phone: str
            Telefone do usuário
        """

        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
    
    @property
    def name(self) -> str:

        """Obtém o nome completo do usuário

        Returns
        -------
        str
            Nome completo do usuário
        
        """

        return self.__name

    @property
    def email(self) -> str:

        """Obtém o e-mail do usuário

        Returns
        -------
        str
            E-mail do usuário
        
        """

        return self.__email

    @property
    def password(self) -> str:

        """Obtém a senha do usuário

        Returns
        -------
        str
            Senha do usuário
        
        """

        return self.__password

    @property
    def phone(self) -> str:

        """Obtém o telefone do usuário

        Returns
        -------
        str
            telefone do usuário
        
        """

        return self.__phone