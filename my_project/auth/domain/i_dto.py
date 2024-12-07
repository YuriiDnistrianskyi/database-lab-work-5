"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import abstractmethod
from typing import Dict


class IDto():

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        pass

    @staticmethod
    @abstractmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        pass
