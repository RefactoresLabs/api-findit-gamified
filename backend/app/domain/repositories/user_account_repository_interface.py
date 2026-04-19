from abc import ABC, abstractmethod

from backend.app.domain.entities.user_account import UserAccount

class UserAccountRepositoryInterface(ABC):

    @abstractmethod
    def create_new_user_account(self, user_account: UserAccount) -> UserAccount: ...

    @abstractmethod
    def update_user_account(self, user_account: UserAccount, id: int) -> UserAccount: ...

    @abstractmethod
    def get_user_account_by_id(self, id: int) -> UserAccount: ...