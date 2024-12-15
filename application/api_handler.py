import requests

class APIHandler:
    """
    Handles interactions with external APIs.

    Attributes:
        base_url (str): Base URL of the external API.
    """

    def __init__(self, base_url):
        """
        Initialize the API handler.

        Args:
            base_url (str): The API's base URL.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        """
        Make a GET request to the API.

        Args:
            endpoint (str): API endpoint.
            params (dict): Query parameters.
            headers (dict): Custom headers.

        Returns:
            dict: JSON response from the API.

        Raises:
            RuntimeError: If the API request fails.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"API GET request failed: {str(e)}")

    def post(self, endpoint, data=None, headers=None):
        """
        Make a POST request to the API.

        Args:
            endpoint (str): API endpoint.
            data (dict): Request payload.
            headers (dict): Custom headers.

        Returns:
            dict: JSON response from the API.

        Raises:
            RuntimeError: If the API request fails.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"API POST request failed: {str(e)}")
