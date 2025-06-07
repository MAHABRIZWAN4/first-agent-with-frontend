# main.py
from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import asyncio

load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY or not isinstance(GEMINI_API_KEY, str):
    raise ValueError("GEMINI_API_KEY is missing or invalid. Please set it as a Streamlit secret.")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

assistant = Agent(
    name="Assistant",
    instructions="You job is to assist the user with their queries. You are a helpful assistant.",
    model=model
)

async def get_ai_response(user_input: str) -> str:
    result = await Runner.run(assistant, user_input, run_config=config)
    return result.final_output
