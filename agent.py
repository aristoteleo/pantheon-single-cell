import asyncio

from pantheon.agent import Agent
from pantheon.tools.python import PythonInterpreterToolSet
from pantheon.remote import run_toolsets

instructions = """You are a AI-agent for analyzing single-cell RNA-seq data.

Given a single-cell RNA-seq dataset,

you can write python code call scanpy package to analyze the data.

Basicly, given a single-cell RNA-seq dataset in h5ad / 10x format or other formats,
you should firstly output your plan and the code.
Then, you should execute the code to read the data,
then preprocess the data, and cluster the data, and finally visualize the data.
"""

toolset = PythonInterpreterToolSet("scanpy-python-interpreter")

agent = Agent(
    name="chiron",
    instructions=instructions,
    model="gpt-4o",
)

async def main():
    async with run_toolsets([toolset]):
        await agent.remote_toolset(toolset.service_id)
        await agent.chat()


if __name__ == "__main__":
    asyncio.run(main())
