class HttpResponse:

    """Encapsula os dados da resposta HTTP"""

    def __init__(self, status_code: int, body: dict[str, any] | None=None) -> None:

        """Inicializa os atributos de instância de HttpResponse

        Parameters
        ----------
        status_code: int
            Código de status da resposta HTTP

        body: dict[str, any] (padrão: None)
            Corpo da resposta HTTP.
        
        """

        self.__status_code = status_code
        self.__body = dict(body) if body else {}
    
    @property
    def status_code(self) -> int:

        """Obtém o código de status de uma resposta HTTP

        Returns
        -------
        dict[str, any]
            Corpo da resposta HTTP
            
        """

        return self.__status_code
    
    @property
    def body(self) -> dict[str, any] :

        """Obtém o corpo de uma resposta HTTP

        Returns
        -------
        dict[str, any]
            Corpo da resposta HTTP

        """

        return self.__body.copy()
