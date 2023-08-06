"""
     The main configuration class for Flask-JWT-Router
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List

from ._entity import _ORMType


class Config:
    """
    :param secret_key: Defaults to `DEFAULT_SECRET_KEY`
    :param entity_key: The name of the model's entity attribute
    :param whitelist_routes: List of tuple pairs of verb & url path
    :param api_name: the api name prefix e.g `/api/v1`
    :param ignored_routes: Opt our routes from api name prefixing
    :param entity_models: Multiple entities to be authenticated
    """
    def __init__(self,
                 secret_key=None,
                 entity_key="id",
                 whitelist_routes=None,
                 api_name=None,
                 ignored_routes=None,
                 entity_models=None,
                 ):

        self.secret_key = secret_key
        self.entity_key = entity_key
        self.whitelist_routes = whitelist_routes
        self.api_name = api_name
        self.ignored_routes = ignored_routes
        self.entity_models = entity_models


class BaseExtension(ABC):
    """Abstract Base Class for Extensions"""
    @abstractmethod
    def init_extensions(self, config: Dict[str, Any], **kwargs) -> Config:
        # pylint: disable=missing-function-docstring
        pass


class Extensions(BaseExtension):
    """Contains the main configuration values"""
    entity_models: List[_ORMType]

    def init_extensions(self, config: Any, **kwargs) -> Config:
        """
        :param config:
        :return:
        """
        entity_models = kwargs.get("entity_models")
        return Config(
            config.get("SECRET_KEY") or "DEFAULT_SECRET_KEY",
            config.get("ENTITY_KEY") or "id",
            config.get("WHITE_LIST_ROUTES") or [],
            config.get("JWT_ROUTER_API_NAME"),
            config.get("IGNORED_ROUTES") or [],
            entity_models or config.get("ENTITY_MODELS") or [],
        )
