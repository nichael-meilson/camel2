"""
Michael Neilson <github: nichael-meilson>
2022-06-30
"""
import pytest

from httpx import AsyncClient
from fastapi import FastAPI

from starlette.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_200_OK,
)
from app.models.articles import CreateArticle, ArticleInDB, GetArticle

# decorate all tests with @pytest.mark.asyncio
pytestmark = pytest.mark.asyncio


@pytest.fixture
def new_article():
    return CreateArticle(
        id=1,
        name="string",
        species="string",
        goal="Study Evolution(ary Processes)",
        num_lines=0,
        setup="string",
        recipient="string",
        medium="string",
        selective_condition="string",
        cripple_mutant=True,
        how_cripple_mutant="string",
        changing_env=True,
        how_changing_env="string",
        env_type="string",
        how_type_env="string",
        complex_stressors=True,
        how_complex_stressors="string",
        num_generations=0,
        abs_time=0,
        contamination="string",
        fitness=True,
        fitness_param="string",
        competition="string",
        mutation_tracking="string",
        wgs=True,
        wgs_tech="string",
        wgs_platform="string",
        num_clones=0,
        num_populations=0,
        cov_clones=0,
        cov_populations=0,
        detection_lim=0,
        ngs_data_link="string",
        max_pop_size=0,
        min_pop_size=0,
        major_outcome="string",
        remarks="string",
        complete_mutation_data=True,
        reference_id="string",
        pmid="string",
        paper_url="string",
    )


class TestCleaningsRoutes:
    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("articles:create-article"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_invalid_input_raises_error(
        self, app: FastAPI, client: AsyncClient
    ) -> None:
        res = await client.post(app.url_path_for("articles:create-article"), json={})
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY


class TestCreateArticle:
    async def test_valid_input_creates_article(
        self, app: FastAPI, client: AsyncClient, new_article: CreateArticle
    ) -> None:
        res = await client.post(
            app.url_path_for("articles:create-article"),
            json={"new_article": new_article.dict()},
        )
        assert res.status_code == HTTP_201_CREATED
        created_article = ArticleInDB(**res.json())
        new_article_response = ArticleInDB(**new_article.dict())
        assert created_article == new_article_response

    @pytest.mark.parametrize(
        "invalid_payload, status_code",
        (
            (None, 422),
            ({}, 422),
            ({"name": "test_name"}, 422),
            ({"price": 10.00}, 422),
            ({"name": "test_name", "description": "test"}, 422),
        ),
    )
    async def test_invalid_input_raises_error(
        self, app: FastAPI, client: AsyncClient, invalid_payload: dict, status_code: int
    ) -> None:
        res = await client.post(
            app.url_path_for("articles:create-article"),
            json={"new_article": invalid_payload},
        )
        assert res.status_code == status_code


class TestGetArticle:
    async def test_get_article_by_author(
        self, app: FastAPI, client: AsyncClient
    ) -> None:
        res = await client.get(
            app.url_path_for("article:get-article"), params={"id": 1}
        )
        assert res.status_code == HTTP_200_OK
        article = GetArticle(**res.json())
        assert article.id == 1


class TestGetAllArticles:
    async def test_get_all_articles(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get(app.url_path_for("articles:get-article"))
        assert res.status_code == HTTP_200_OK
        cleaning = [GetArticle(**article) for article in res.json()]
        # TODO think of another test here
        assert len(cleaning) > 0
