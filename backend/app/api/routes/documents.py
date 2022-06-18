'''
Michael Neilson <github: nichael-meilson>
2022-06-18
'''
from typing import List

from fastapi import APIRouter


router = APIRouter()




@router.get("/")
async def get_articles() -> List[dict]:
    articles = [
        {"id": 1, "author": "Charles Darwin", "title": "Origin of Species", "date": "1900-01-01"},
        {"id": 2, "author": "Sigmund Freud", "title": "Mommy Issues", "date": "1900-01-02"}
    ]

    return articles

