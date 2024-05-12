import config
from common import json
from common import logger
from database import Base
from database import SessionLocal
from database import engine
from models import Anime
from models import Character
from models import Quote


def _dump_quote(db: SessionLocal, quote: dict[str, str]):
    logger.debug("_dump_quote%s", locals())

    existing_anime = db.query(Anime).filter(Anime.name == quote["anime"]).first()
    if existing_anime is None:
        new_anime = Anime(name=quote["anime"])
        db.add(new_anime)
        db.flush()
        anime_id = new_anime.id
    else:
        anime_id = existing_anime.id

    existing_character = (
        db.query(Character).filter(Character.name == quote["character"]).first()
    )
    if existing_character is None:
        new_character = Character(name=quote["character"], anime_id=anime_id)
        db.add(new_character)
        db.flush()
        character_id = new_character.id
    else:
        character_id = existing_character.id

    existing_quote = db.query(Quote).filter(Quote.content == quote["quote"]).first()
    if existing_quote is None:
        db.add(
            Quote(content=quote["quote"], anime_id=anime_id, character_id=character_id)
        )
        db.flush()


def dump_database(data_path: str = config.DATA_PATH):
    logger.debug("dump_database%s", locals())

    with open(data_path, "rb") as file:
        quotes = json.load(file)

    load_database()
    db = SessionLocal()

    for quote in quotes:
        _dump_quote(db, quote)

    db.commit()


def load_database():
    Base.metadata.create_all(engine)


def main():
    dump_database()


if __name__ == "__main__":
    main()
