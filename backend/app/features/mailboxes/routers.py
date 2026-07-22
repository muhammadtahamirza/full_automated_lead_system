from core.routers import build_crud_router, db_session
from .models import CreateMail, UpdateMail, MailAccount
from .services import loginMailbox
from fastapi import HTTPException, status

mailRouter = build_crud_router(
	model=MailAccount,
    create_schema=CreateMail,
    update_schema=UpdateMail,
    prefix="/mailaccount",
    tag="MailAccounts",
	exclude_routes=["create"]  # will use our own
)


@mailRouter.post("")
def create_mailbox(mailbox : CreateMail, db : db_session):

	try:
		loginMailbox(mailbox)
	except ValueError as err:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=str(err)
		)
	try:
		new_account = MailAccount.model_validate(mailbox)

		db.add(new_account)
		db.commit()
		db.refresh(new_account)
	except Exception as db_err:
		db.rollback()
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="Failed to save data safely to the database."
		)

	return {"status": "mailbox created"}




