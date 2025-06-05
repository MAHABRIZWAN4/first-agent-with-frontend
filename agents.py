import httpx
import os

class AsyncOpenAI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.openai_client = openai_client

class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

class Runner:
    @staticmethod
    async def run(agent, user_input, run_config=None):
        url = f"{agent.model.openai_client.base_url}models/{agent.model.model}:generateContent"
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": agent.model.openai_client.api_key,
        }
        data = {
            "contents": [
                {"parts": [{"text": f"{agent.instructions}\nUser: {user_input}"}]}
            ]
        }
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, headers=headers, json=data)
                response.raise_for_status()
                result = response.json()
                try:
                    final_output = result["candidates"][0]["content"]["parts"][0]["text"]
                except Exception:
                    final_output = "Sorry, I couldn't parse the response from Gemini."
        except httpx.HTTPStatusError as e:
            final_output = f"HTTP error: {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            final_output = f"Request error: {str(e)}"
        except Exception as e:
            final_output = f"Unexpected error: {str(e)}"
        class Result:
            pass
        Result.final_output = final_output
        return Result()

class RunConfig:
    def __init__(self, model, model_provider, tracing_disabled=True):
        self.model = model
        self.model_provider = model_provider
        self.tracing_disabled = tracing_disabled