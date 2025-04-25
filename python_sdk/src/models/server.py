"""
Server Model Module

This module provides the Server model class for handling server configuration information.
"""

from typing import Dict


class Server:
    """
    A class that encapsulates server configuration information.
    
    This class stores and manages server connection details including server name
    and site information for connecting to the VizQL Data Service API.
    
    Attributes:
        server_name (str): The server's URL or hostname
        site (str): The site name or identifier
    """
    
    def __init__(self, server_name: str, site: str):
        """
        Initialize a new Server instance.
        
        Args:
            server_name: The server's URL or hostname
            site: The site name or identifier
        """
        self.server_name = server_name
        self.site = site

    def __str__(self) -> str:
        """
        Return a string representation of the server.
        
        Returns:
            str: A formatted string containing server details
        """
        return f"Server: {self.server_name}\nSite: {self.site}"

    def get_server_info(self) -> Dict[str, str]:
        """
        Get a dictionary containing the server's configuration information.
        
        Returns:
            Dict[str, str]: A dictionary with server configuration details
        """
        return {
            'serverName': self.server_name,
            'site': self.site
        }
