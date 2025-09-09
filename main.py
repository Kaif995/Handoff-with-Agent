from agents import Agent,RunContextWrapper,Runner,function_tool,AsyncOpenAI,OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled
import os
from dotenv import load_dotenv
import asyncio
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

set_tracing_disabled(True)
load_dotenv()

# Access environment variables
key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("base_url")

# Initialize Gemini client
gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

# Define model
Model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client
)


async def main():

   
    medical_Assistant=Agent(
        name="Medical",
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful Medical assiatant.""",
    handoff_description="This is an Medical Assistant",
        model=Model
    )
    computing_Assistant=Agent(
        name="computer",
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful Computer Science assiatant.""",
    handoff_description="This is an Computing Assistant",
        model=Model
    )
    agent=Agent(
        name="Kaif Shamim",
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assiatant.""",
        handoffs=[medical_Assistant,computing_Assistant],
        handoff_description="This is an helpful Assistant",
        model=Model
    )

  
    result= await Runner.run(
        starting_agent=agent,
        input="tell me about frontend developer"
    )
    print(result.last_agent.name)
    print(result.final_output)
   





asyncio.run(main())  
