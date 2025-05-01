"""
Endpoints for VizQL Data Service REST APIs.

This module defines the API endpoints used for interacting with the VizQL Data Service.
It provides a centralized location for all endpoint paths to ensure consistency
across the application.

Available Endpoints:
- VIZQL_DATA_SERVICE_URL: Base URL for the VizQL Data Service
- QUERY_DATASOURCE_ENDPOINT: Endpoint for querying data sources
- READ_METADATA_ENDPOINT: Endpoint for reading metadata
"""


class EndPoints:
    VIZQL_DATA_SERVICE_URL = "/api/v1/vizql-data-service"
    QUERY_DATASOURCE_ENDPOINT = "/query-datasource"
    READ_METADATA_ENDPOINT = "/read-metadata"
