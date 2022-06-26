'''
Michael Neilson <github: nichael-meilson>
2022-06-18
'''
from pydantic import BaseModel


class IDModelMixin(BaseModel):
    id: str

