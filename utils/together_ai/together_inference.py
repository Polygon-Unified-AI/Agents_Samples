import requests
from os import environ
import json

import sseclient

from .together_models import TogetherChatModel, TogetherCompletionModel
from .message import Message, Role

# Api endpoint for chat completions
_API_CHAT_ENDPOINT = "https://api.together.xyz/v1/chat/completions"

# Environment variable key
# the environment variable with this key should be set to the API token
TOGETHER_ENV_VARIABLE_KEY = "TOGETHER_API_TOKEN"

class TogetherInference:
    @staticmethod
    def complete_chat(
        messages: list[Message],
        model: TogetherChatModel,
        max_tokens: int = 100,
        temperature: float = 0.0,
    )-> dict:
        try:
            response = requests.post(
                _API_CHAT_ENDPOINT,
                json={
                    "model": model.value,
                    "messages": [message.to_dict() for message in messages],
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": 0.7,
                    "top_k": 50,
                    "repetition_penalty": 1,
                },
                headers={
                    "Authorization": f"Bearer {environ[TOGETHER_ENV_VARIABLE_KEY]}",
                },
            )

            response_json: dict = response.json()

            if "error" in response_json.keys():
                if "due to rate limiting" in response_json["error"]:
                    return TogetherInference.chat_complete(messages, model, max_tokens)

                raise Exception(response_json["error"])

            return response_json

        except Exception as e:
            return f"Unexpected error occurred: {e}"
        
        
    @staticmethod
    def complete_chat_stream(
        messages: list[Message],
        model: TogetherChatModel,
        max_tokens: int = 100,
        temperature: float = 0.0,
    ):
        try:
            response = requests.post(
                _API_CHAT_ENDPOINT,
                json={
                    "model": model.value,
                    "messages": [message.to_dict() for message in messages],
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": 0.7,
                    "top_k": 50,
                    "repetition_penalty": 1,
                    "stream": True,
                },
                headers={
                    "Authorization": f"Bearer {environ[TOGETHER_ENV_VARIABLE_KEY]}",
                    "Accept": "text/event-stream",
                },
                stream=True,
            )
        except Exception as e:
            print("Error in TogetherInference ", e)
            raise e
        
        response.raise_for_status()
        
        client = sseclient.SSEClient(response)
        
        chat_response = ""
        for event in client.events():
            if event.data == "[DONE]":
                break

            try:
                chat_response += json.loads(event.data)["choices"][0]["text"]
                yield json.loads(event.data)
            except:
                pass
            