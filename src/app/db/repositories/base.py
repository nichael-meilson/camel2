"""
Michael Neilson <github: nichael-meilson>
2022-06-25
"""
from databases import Database


class BaseRepository:
    def __init__(self, db: Database) -> None:
        self.db = db
