from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.entities.user_account import UserAccount

from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel

from sqlalchemy.orm import Session

class UserAccountRepository(UserAccountRepositoryInterface):

    """Lida com as transações de persistência da entidade UserAccount"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância da classe UserAccountRepository

        Parameters
        ----------
        session: Session
            Sessão atual que lida com as transações

        """

        self.__session = session

    def create_new_user_account(self, user_account: UserAccount) -> None:

        """Cria uma nova instância da tabela user_account

        Parameters
        ----------
        user_account: UserAccount
            Objeto da entidade conta de usuário com os dados a serem armazenados
        
        Returns
        -------
        UserAccount
            Objeto da entidade conta de usuário com os dados armazenados
        """

        user_account_registry = UserAccountModel(
            name=user_account.name,
            email=user_account.email,
            password=user_account.password,
            phone=user_account.phone,
        )

        self.__session.add(user_account_registry)
    
    def update_user_account(self, user_account: UserAccount, id: int) -> UserAccount:

        """Atualiza uma instância da tabela user_account através do ID

        Parameters
        ----------
        user_account: UserAccount
            Objeto da entidade conta de usuário com os dados a serem modificados
        
        id: int
            ID da conta do usuário a ser atualizada

        Returns
        -------
        UserAccount
            Objeto da entidade conta de usuário com os dados atualizados
        
        """
        pass

    def get_user_account_by_id(self, id: int) -> UserAccount:

        """Obtém uma instância da tabela user_account através do ID

        Parameters
        ----------
        id: int
            ID da conta do usuário a ser obtida

        Returns
        -------
        UserAccount
            Objeto da entidade conta de usuário com os dados buscados
        
        """

        pass
    

