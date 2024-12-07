from sqlalchemy import inspect
from sqlalchemy.orm import Mapper
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.park_attraction import ParkAttraction


class ParkAttractionDAO(GeneralDAO):
    _domain_type = ParkAttraction

    def get_by_two_id(self, park_id: int, attraction_id: int) -> ParkAttraction:
        return self._session.query(ParkAttraction).filter(
            ParkAttraction.park_id == park_id,
            ParkAttraction.attraction_id == attraction_id
        ).one()


    def uptade_by_two_id(self, park_id: int, attraction_id: int, in_obj: object) -> None:
        domain_obj = self._session.query(ParkAttraction).filter(
            ParkAttraction.park_id == park_id,
            ParkAttraction.attraction_id == attraction_id
        ).one() #
        mapper: Mapper = inspect(type(in_obj))  # Metadata
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()


    def delete_by_two_id(self, park_id: int, attraction_id: int) -> None:
        domain_obj = self._session.query(self._domain_type).filter(ParkAttraction.park_id == park_id).filter(ParkAttraction.attraction_id == attraction_id).one()
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
