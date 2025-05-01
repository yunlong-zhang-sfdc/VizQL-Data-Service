"""
Abstract base class for VizQL Data Service HTTP clients.

This module defines an abstract base class for implementing HTTP clients for the VizQL Data Service.
It provides two abstract methods that must be implemented by subclasses:
- query_datasource: Query data sources
- read_metadata: Read metadata

All concrete HTTP client implementations should inherit from this base class and implement these methods.
"""

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
