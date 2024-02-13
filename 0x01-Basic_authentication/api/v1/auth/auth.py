"""
    This module is the template for all authentication systems.
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    This class provides authentication functionality for the API.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths that
                are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request (flask.Request, optional): The request object.
                Defaults to None.

        Returns:
            str: The authorization header value.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.

        Args:
            request (flask.Request, optional): The request object.
                Defaults to None.

        Returns:
            User: The current user object.
        """
        return None
