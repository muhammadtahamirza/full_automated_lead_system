from typing import Annotated, Type
from sqlmodel import Session, select
from sqlmodel import SQLModel

class repository[anytable : SQLModel]:
	"""generic class for crud operatoins for each table"""

	def __init__(self, session: Session, table: Type[anytable]):
		self.db = session
		self.table = table

	"""create method"""
	def create_row(self, entry : anytable):
		self.db.add(entry)
		self.db.commit()
		self.db.refresh(entry)
		return entry

	"""read methods"""
	def get_row_from_id(self, id: int) -> dict:
		row= self.db.get(self.table,id)
		return row

	def get_all_rows(self) :
		statement = select(self.table)
		return self.db.exec(statement).all()

	"""update methods"""
	def update_row(self, id : int, row_details : anytable   ):
		row = self.get_row_from_id(id)
		if not row:
			return {
				"status" : "Not found"
			}
		dict_row = row_details.model_dump(exclude_unset=True)
		for key , value in dict_row.items():
			setattr(row, key, value)

		self.db.commit()
		self.db.refresh(row)
		return row

	"""delete method"""
	def delete_row(self, id : int):
		row = self.get_row_from_id(id)
		if not row :
			return {
				"status" : "not found"
			}
		self.db.delete(row)
		self.db.commit()
		return {"status" : "success"}