"""
Utility Module

This module provides utility functions for the SDK.
"""


def format_server_url(url: str, subdomain: str = "") -> str:
    """Format server URL with proper protocol and subdomain.

    Args:
        url: The server URL to format
        subdomain: Optional subdomain to append to the URL

    Returns:
        str: Formatted URL with proper protocol and subdomain

    Raises:
        ValueError: If URL is empty or contains spaces
        TypeError: If URL is None
    """
    if url is None:
        raise TypeError("URL must be a string")

    if not url:
        raise ValueError("URL cannot be empty")

    if " " in url:
        raise ValueError("Invalid URL format")

    # Handle server URL protocol and domain
    if "online.tableau.com" in url and not url.startswith("https"):
        url = f"https://{url}"
    elif not url.startswith(("http://", "https://")):
        url = f"http://{url}"

    # Remove trailing slash if present
    url = url.rstrip("/")

    # Append subdomain if provided
    if subdomain:
        # Ensure subdomain starts with a slash
        if not subdomain.startswith("/"):
            subdomain = f"/{subdomain}"
        url = f"{url}{subdomain}"

    return url
