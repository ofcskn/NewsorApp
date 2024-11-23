from application.api_handler import APIHandler
from decouple import config

class ChatGPTService:
    """
    Application layer for interacting with OpenAI's ChatGPT API.

    Attributes:
        api_handler (APIHandler): Handles external API requests.
    """

    def __init__(self):
        """
        Initialize the ChatGPTService with OpenAI's API base URL.
        """
        base_url = "https://api.openai.com/v1"
        self.api_handler = APIHandler(base_url)
        self.api_key = config('OPENAI_API_KEY')

    def get_chat_response(self, messages):
        """
        Get a response from ChatGPT based on user messages.

        Args:
            messages (list): List of messages in the format required by OpenAI.

        Returns:
            dict: ChatGPT response.

        Raises:
            RuntimeError: If the API call fails.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"model": "gpt-4", "messages": messages}
        return self.api_handler.post("chat/completions", data=data, headers=headers)
