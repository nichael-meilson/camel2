'''
Michael Neilson <github: nichael-meilson>
2022-06-18
'''
from fastapi import APIRouter

from app.api.routes.articles import router as documents_router


router = APIRouter()


router.include_router(documents_router, prefix="/article", tags=["articles"])

