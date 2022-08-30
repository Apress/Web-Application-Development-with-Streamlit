from sqlalchemy import Column, Integer, String
from .Base import Base


class Employees(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    date_of_birth = Column(String, default=True)
    paygrade_id = Column(Integer, unique=True, index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "paygrade_id": self.paygrade_id
        }
