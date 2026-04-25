from datetime import date

from backend.app.infrastructure.persistence.models.base import Base

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text, Date, ForeignKey


class ItemModel(Base):

    """Representa uma classe mapeada com a tabela item"""

    __tablename__ = "item"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    description = mapped_column(Text, nullable=True)
    registry_date = mapped_column(Date, nullable=False)
    category_id = mapped_column(Integer, ForeignKey("category.id"), nullable=False)
    account_id = mapped_column(Integer, ForeignKey("user_account.id"), nullable=False)

    def __repr__(self) -> str:

        """Representa o objeto ItemModel em uma String Literal

        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"Item=[{self.id}, {self.name}, {self.registry_date}]"
