from sqlalchemy import Column, Integer, String
from .Base import Base


class Admins(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)

    username = Column(String)
    password_hash = Column(String, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash
        }
