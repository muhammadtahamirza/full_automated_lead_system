# core/crud_router.py
from typing import Type, TypeVar, Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import SQLModel, Session
from .database import get_session
from .repository import repository

db_session = Annotated[Session, Depends(get_session)]

ModelT = TypeVar("ModelT", bound=SQLModel)
CreateT = TypeVar("CreateT", bound=SQLModel)
UpdateT = TypeVar("UpdateT", bound=SQLModel)

def build_crud_router(
    *,
    model: Type[ModelT],
    create_schema: Type[CreateT],
    update_schema: Type[UpdateT],
    prefix: str,
    tag: str,
    exclude_routes: List[str] = None, # Added exclusion list
) -> APIRouter:
    router = APIRouter(prefix=prefix, tags=[tag])
    excluded = exclude_routes or []

    # Only build POST if it is not excluded
    if "create" not in excluded:
        @router.post("", response_model=model, status_code=status.HTTP_201_CREATED)
        def create(payload: create_schema, session: db_session):  # type: ignore[valid-type]
            repo = repository(session, model)
            db_obj = model(**payload.model_dump())
            return repo.create_row(db_obj)

    if "read_all" not in excluded:
        @router.get("", response_model=list[model])
        def read_all(session: db_session):
            repo = repository(session, model)
            return repo.get_all_rows()

    if "read_by_id" not in excluded:
        @router.get("/{id}", response_model=model)
        def read_by_id(id: int, session: db_session):
            repo = repository(session, model)
            row = repo.get_row_from_id(id)
            if not row:
                raise HTTPException(404, f"{model.__name__} not found")
            return row

    if "update" not in excluded:
        @router.put("/{id}", response_model=model)
        def update(id: int, payload: update_schema, session: db_session):  # type: ignore[valid-type]
            repo = repository(session, model)
            row = repo.update_row(id, payload)
            if not row:
                raise HTTPException(404, f"{model.__name__} not found")
            return row

    if "delete" not in excluded:
        @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
        def delete(id: int, session: db_session):
            repo = repository(session, model)
            success = repo.delete_row(id)
            if not success:
                raise HTTPException(404, f"{model.__name__} not found")
            return None

    return router
