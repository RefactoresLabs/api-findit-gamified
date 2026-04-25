from abc import ABC, abstractmethod


from backend.app.domain.entities.category import Category


class CategoryRepositoryInterface(ABC):

    @abstractmethod
    def get_category_by_id(self, id: int) -> Category: ...