from fastapi import APIRouter

from .product import product_router

router: APIRouter = APIRouter(prefix="/v1")
router.include_router(product_router)