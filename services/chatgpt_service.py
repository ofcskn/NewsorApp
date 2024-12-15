from application.api_handler import APIHandler
from decouple import config
from openai import OpenAI

# implement openai
client = OpenAI(api_key=config('OPENAI_API_KEY'), organization=config('OPENAI_ORG_ID'), project=config('OPENAI_PROJECT_ID'))
print(client)
class ChatGPTService:
    """
    Application layer for interacting with OpenAI's ChatGPT API.

    Attributes:
        api_handler (APIHandler): Handles external API requests.
    """

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
        print(messages)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        print(completion.choices[0].message)
        return completion
