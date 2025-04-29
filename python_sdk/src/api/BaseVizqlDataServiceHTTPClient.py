from abc import ABC, abstractmethod
from typing import Any, Optional, Dict


class BaseVizqlDataServiceHTTPClient(ABC):

    @abstractmethod
    def query_datasource(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        pass

    @abstractmethod
    def read_metadata(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        pass
