import asyncio
import os
from fastmcp import Client
from openai import OpenAI

async def main():
    client = OpenAI()
    mcp_url = os.environ.get("MCP_URL", "http://localhost:8000/mcp")

    resp = await client.responses.create(
        model="gpt-4o",
        tools=[
            {
                "type": "mcp",
                "server_label": "count_r_server",
                "server_url": mcp_url,
                "require_approval": "never"
            },
        ],
        input="Count the number of times the letter 'R' appears in the following text: 'Rapidly running rabbits rapidly run.'"
    )

    print(resp)

if __name__ == "__main__":
    asyncio.run(main())