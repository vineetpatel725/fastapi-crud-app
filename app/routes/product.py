from fastapi import APIRouter, status, Depends, Query, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import desc, asc
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.schemas import product as ps
from app.models import product as pm
from app.db import get_session
from app.config import logger

product_router: APIRouter = APIRouter(tags=["Product"])


@product_router.post(
    path="/product",
    name="Create Product",
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product: ps.Product,
    session: Session = Depends(get_session)
) -> JSONResponse:
    """
    API to register new product.
    :param product: Product Details like category, name and price.
    :return: Return JSON Response based on the operation execution. i.e. 201 on success, 
    409 on duplicate product
    """
    logger.info(f"API Request Received", request=product)
    response: dict = {
        "status": "success",
        "code": status.HTTP_201_CREATED,
        "data": None
    }    
    try:
        product: pm.Product = pm.Product(
            name=product.name,
            category=product.category,
            price=product.price
        )
        session.add(product)
        session.commit()
        session.refresh(product)
        response['data'] = jsonable_encoder(product)
    except IntegrityError as e:
        session.rollback()
        response.update(status='failure', code=status.HTTP_409_CONFLICT)
    except Exception as e:
        session.rollback()        
        response.update(status='failure', code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.exception(f"API Request Failed :: {e}")
    finally:
        logger.info(f"API Request Completed", response=response)
        return JSONResponse(
            status_code=response['code'],
            content=response
        )


@product_router.get(
    path="/products",
    name="Get Products",
    status_code=status.HTTP_200_OK
)
def get_products(
    page_no: int = Query(default=1, title="Page No.", gt=0),
    per_page: int = Query(default=10, title="Page Records", gt=0),
    sort: int = Query(default=0, title="Sort", ge=0, le=1),
    sort_by: str = Query(default="name", title="Sort By"),
    session: Session = Depends(get_session)
) -> JSONResponse:
    """
    API to fetch all product with pagination and filter support.
    :param page_no: Page Number
    :param per_page: Total nuber records tobe retrived per page.
    :param sort: Sort records by ascending or descending
    :param sort_by: Sorting tobe applied
    :return: Return JSON Response based on the operation execution. i.e. 200 on success, 
    404 on no records found
    """
    logger.info(
        f"API Request Received", 
        request={"page_no": page_no, "per_page": per_page, "sort": sort, "sort_by": sort_by}
    )
    response: dict = {
        "status": "success",
        "code": status.HTTP_200_OK,
        "data": None
    }    
    try:
        sort_columns: list = ["name", "category", "price"]
        if sort_by in sort_columns:
            sort_by = eval(f"pm.Product.{sort_by}")
        else:
            sort_by = pm.Product.id        
        if sort == 0:
            order_by = (asc(sort_by))
        else:
            order_by = (desc(sort_by))
                    
        products = session.query(pm.Product).order_by(
            order_by
        ).limit(
            per_page
        ).offset(
            (page_no - 1)*per_page
        ).all()                
        response['data'] = jsonable_encoder(products)
    except Exception as e:        
        response.update(status='failure', code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.exception(f"API Request Failed :: {e}")
    finally:
        logger.info(f"API Request Completed", response=response)
        return JSONResponse(
            status_code=response['code'],
            content=response
        )
    

@product_router.get(
    path="/product/{id}",
    name="Get Product",
    status_code=status.HTTP_200_OK
)
def get_product(
    id: int = Path(default=..., title="Product ID", gt=0),
    session: Session = Depends(get_session)
) -> JSONResponse:
    """
    API to fetch particular product details by id.
    :param id: Id of a product tobe fetched.
    :return: Return JSON Response based on the operation execution. i.e. 200 on success
    """
    response: dict = {
        "status": "success",
        "code": status.HTTP_200_OK,
        "data": None
    }    
    try:
        product = session.query(pm.Product).where(pm.Product.id==id).one()
        response['data'] = jsonable_encoder(product)
    except NoResultFound as e:        
        response.update(status='failure', code=status.HTTP_404_NOT_FOUND)
    except Exception as e:        
        response.update(status='failure', code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.exception(f"API Request Failed :: {e}")
    finally:
        logger.info(f"API Request Completed", response=response)
        return JSONResponse(
            status_code=response['code'],
            content=response
        )   


@product_router.delete(
    path="/product/{id}",
    name="Delete Product",
    status_code=status.HTTP_200_OK
)
def delete_products(
    id: int = Path(default=..., title="Product ID", gt=0),
    session: Session = Depends(get_session)
) -> JSONResponse:
    """
    API to delete particular product by id.
    :param id: Id of a product tobe deleted.
    :return: Return JSON Response based on the operation execution. i.e. 200 on success
    """
    response: dict = {
        "status": "success",
        "code": status.HTTP_200_OK,
        "data": None
    }    
    try:
        product = session.query(pm.Product).where(pm.Product.id==id).one()
        session.delete(product)
        session.commit()
    except NoResultFound as e:                
        response.update(status='failure', code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        session.rollback()        
        response.update(status='failure', code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.exception(f"API Request Failed :: {e}")
    finally:
        logger.info(f"API Request Completed", response=response)
        return JSONResponse(
            status_code=response['code'],
            content=response
        )