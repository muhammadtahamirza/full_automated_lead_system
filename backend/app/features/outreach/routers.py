from core.routers import build_crud_router
from .models import CreateTemplate, UpdateTemplate, Template


outreachRouter = build_crud_router(
	model=Template,
    create_schema=CreateTemplate,
    update_schema=UpdateTemplate,
    prefix="/template",
    tag="Templates",

)

