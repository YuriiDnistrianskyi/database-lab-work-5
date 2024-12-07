"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List, Dict

from http import HTTPStatus
from flask import abort


class GeneralController(ABC):
    _service = None



