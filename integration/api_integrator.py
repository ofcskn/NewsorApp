from application.api_handler import PythonAPIHandler

class APIIntegrator:
    """
    Integrates external APIs with application logic.
    """

    def __init__(self, base_url):
        """
        Initialize the API integrator with a base URL.

        Args:
            base_url (str): Base URL of the external API.
        """
        self.api_handler = PythonAPIHandler(base_url)

    def fetch_and_process_data(self, endpoint):
        """
        Fetch data from an external API and process it.

        Args:
            endpoint (str): API endpoint to query.

        Returns:
            dict: Processed API response data.

        Raises:
            RuntimeError: If integration fails.
        """
        try:
            data = self.api_handler.get_data(endpoint)
            return data
        except Exception as e:
            raise RuntimeError(f"Integration failed: {str(e)}")
