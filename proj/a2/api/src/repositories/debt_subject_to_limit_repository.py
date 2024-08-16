from api.src.models.dts_table_models import Debt_Subject_To_Limit
from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class DebtSubjectToLimitRepository(DTSTablesBaseRepository):
    name = "debt_subject_to_limit"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Debt_Subject_To_Limit).all()

    def generate_filter(self):
        pass
