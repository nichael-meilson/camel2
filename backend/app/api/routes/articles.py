'''
Michael Neilson <github: nichael-meilson>
2022-06-18
'''
from typing import List

from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED
from app.models.articles import CreateArticle, ArticleInDB
from app.db.repositories.articles import ArticlesRepository
from app.api.dependencies.database import get_repository


router = APIRouter()


@router.get("/")
async def get_articles() -> List[dict]:
    articles = [
        {"id": 1, "author": "Charles Darwin", "title": "Origin of Species", "date": "1900-01-01"},
        {"id": 2, "author": "Sigmund Freud", "title": "Mommy Issues", "date": "1900-01-02"}
    ]

    return articles


@router.post("/", response_model=ArticleInDB, name="articles:create-article", status_code=HTTP_201_CREATED)
async def create_new_article(
    new_article: CreateArticle = Body(..., embed=True),
    articles_repo: ArticlesRepository = Depends(get_repository(ArticlesRepository)),
) -> ArticleInDB:
    created_article = await articles_repo.create_article(new_article=new_article)
    return created_article
