from core.routers import build_crud_router
from .models import CreateMail, UpdateMail, MailAccount

mailRouter = build_crud_router(
	model=MailAccount,
    create_schema=CreateMail,
    update_schema=UpdateMail,
    prefix="/mailaccount",
    tag="MailAccounts",
)

