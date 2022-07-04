"""
Michael Neilson <github: nichael-meilson>
2022-06-18
"""
from typing import List

from fastapi import APIRouter, Body, Depends, Query, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
from app.models.articles import CreateArticle, ArticleInDB, GetArticle
from app.db.repositories.articles import ArticlesRepository
from app.api.dependencies.database import get_repository


router = APIRouter()


@router.get(
    "s/",
    response_model=List[GetArticle],
    name="articles:get-article",
    status_code=HTTP_200_OK,
)
async def get_articles(
    articles_repo: ArticlesRepository = Depends(get_repository(ArticlesRepository)),
) -> List[GetArticle]:
    articles = await articles_repo.get_all_articles()
    return articles


@router.get(
    "/", response_model=GetArticle, name="article:get-article", status_code=HTTP_200_OK
)
async def get_article(
    articles_repo: ArticlesRepository = Depends(get_repository(ArticlesRepository)),
    id_: str = Query(None, alias="id", description="The ID of the article"),
    author: str = Query(None, description="The name of the author"),
) -> GetArticle | HTTPException | ValueError:
    if author and not id_:
        article = await articles_repo.get_article_from_name(author)
    if id_ and not author:
        article = await articles_repo.get_article_from_id(id_)
    if not author and not id_:
        raise ValueError("Must have one of author or id.")
    if author and id_:
        raise ValueError("Must have only one of author or id.")
    if not article:  # type: ignore
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with that id."
        )
    return article  # type: ignore


@router.post(
    "s/",
    response_model=ArticleInDB,
    name="articles:create-article",
    status_code=HTTP_201_CREATED,
)
async def create_new_article(
    new_article: CreateArticle = Body(..., embed=True),
    articles_repo: ArticlesRepository = Depends(get_repository(ArticlesRepository)),
) -> ArticleInDB:
    created_article = await articles_repo.create_article(new_article=new_article)
    return created_article
