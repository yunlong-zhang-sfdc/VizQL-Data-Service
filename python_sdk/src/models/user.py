"""
User Model Module

This module provides the User model class for handling user authentication information.
"""

from typing import Dict, Optional


class User:
    """
    A class that encapsulates user authentication information.

    This class stores and manages user credentials including username, password,
    and personal access token for authentication with the VizQL Data Service API.

    Attributes:
        username (str): The user's username
        password (str): The user's password
        personal_access_token (str): The user's personal access token
    """

    def __init__(
        self, username: str, password: str, personal_access_token: Optional[str] = None
    ):
        """
        Initialize a new User instance.

        Args:
            username: The user's username
            password: The user's password
            personal_access_token: Optional personal access token for authentication
        """
        self.username = username
        self.password = password
        self.personal_access_token = personal_access_token

    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Returns:
            str: A string containing the username and authentication method
        """
        auth_method = (
            "Personal Access Token" if self.personal_access_token else "Password"
        )
        return f"User: {self.username} (Auth: {auth_method})"

    def get_user_info(self) -> Dict[str, str]:
        """
        Get a dictionary containing the user's authentication information.

        Returns:
            Dict[str, str]: A dictionary with user authentication details
        """
        return {
            "userId": self.username,
            "password": self.password,
            "personal_access_token": self.personal_access_token,
        }
