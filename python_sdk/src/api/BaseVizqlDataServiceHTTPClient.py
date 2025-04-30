from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from openapi_client.models import QueryRequest, ReadMetadataRequest


class BaseVizqlDataServiceHTTPClient(ABC):

    @abstractmethod
    def query_datasource(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        request: Optional[QueryRequest] = None,
    ) -> Any:
        pass

    @abstractmethod
    def read_metadata(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        request: Optional[ReadMetadataRequest] = None,
    ) -> Any:
        pass
