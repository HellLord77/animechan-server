from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from database import Base


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(500), nullable=False, unique=True)


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(500), nullable=False, unique=True)
    anime_id = Column(Integer, ForeignKey("anime.id"), nullable=False)

    anime = relationship("Anime")


class Quote(Base):
    __tablename__ = "quote"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    content = Column(Text, nullable=False)
    anime_id = Column(Integer, ForeignKey("anime.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)

    anime = relationship("Anime")
    character = relationship("Character")
