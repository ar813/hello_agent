import os
from dotenv import load_dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load .env file variables into environment
load_dotenv()

gemini_api_key = os.environ.get("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client # openai_client means: The connection (or client) that talks to the AI server (like Gemini or OpenAI).
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True # Don't keep a detailed history of what the AI does. Just give me the answer quickly.
)

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=model)

result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)

print(result.final_output)


"""
| Item                         | Purpose (Easy Explanation)                                   |
| ---------------------------- | ------------------------------------------------------------ |
| `agents`                     | A toolbox for building AI agents.                            |
| `Agent`                      | Makes the AI assistant with a name, model, and instructions. |
| `Runner`                     | Sends messages to the agent and gets replies.                |
| `AsyncOpenAI`                | Connects to the AI model online using an API key.            |
| `OpenAIChatCompletionsModel` | Tells the agent which model to use (like Gemini).            |
"""

"""
🎯 Purpose of RunConfig in simple words:
RunConfig sets the rules and settings for how the agent should run and behave when it receives a message.

- It's like a settings box that tells the agent:
    - Which model to use,
    - Which provider (like OpenAI or Gemini),
    - Whether to turn on extra features like tracing

"""