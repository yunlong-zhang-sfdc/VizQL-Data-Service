"""
User Model Module

This module provides the User model class for handling user authentication information.
"""

from typing import Dict, Optional


class User:
    """
    A class that encapsulates user authentication information.
    Supports creation via password or personal access token (PAT).
    """

    def __init__(
        self,
        username: str,
        password: Optional[str] = None,
        personal_access_token: Optional[str] = None,
    ):
        self.username = username
        self.password = password
        self.personal_access_token = personal_access_token

    def __str__(self) -> str:
        auth_method = (
            "Personal Access Token" if self.personal_access_token else "Password"
        )
        return f"User: {self.username} (Auth: {auth_method})"

    @classmethod
    def from_password(cls, username: str, password: str):
        return cls(username=username, password=password)

    @classmethod
    def from_pat(cls, token_name: str, personal_access_token: str):
        return cls(username=token_name, personal_access_token=personal_access_token)

    def get_user_info(self) -> Dict[str, Optional[str]]:
        if self.personal_access_token:
            return {
                "token_name": self.username,  # username field used as token_name for PAT
                "personal_access_token": self.personal_access_token,
            }
        elif self.password:
            return {
                "username": self.username,
                "password": self.password,
            }
        else:
            raise ValueError(
                "User must have either a password or a personal access token."
            )
