"""
Client MCP - Count R
-------------------------------------------
This client:
1️. Connects to a MCP Server.
2. Uses tools to count the letter 'R'.
3. Integrates with OpenAI's GPT-4o-mini model to demonstrate tool usage.
"""
import os
import asyncio
from openai import OpenAI
from fastmcp import Client

# os.environ["OPENAI_API_KEY"] = ""
OPENAI_MODEL = "gpt-4o-mini"
MCP_SERVER_URL = os.environ.get("MCP_URL", "http://localhost:8000/mcp")
FASTMCP_API_KEY = os.environ.get("FASTMCP_API_KEY")


async def main():
    # Connect to the MCP server. If the API key is available, pass it.
    if FASTMCP_API_KEY:
        client_mcp = Client(MCP_SERVER_URL, auth=FASTMCP_API_KEY)
        print("Using FastMCP API key for authentication.")
    else:
        client_mcp = Client(MCP_SERVER_URL)

    async with client_mcp:
        print(" Connected to the MCP Count R server")
        text_test = "Rapidly running rabbits rapidly run."
        
        # Call the tool `count_r`
        response = await client_mcp.call_tool(
            "count_r",
            {"text": text_test}
        )
        print(f"Direct TEST - Response from count_r tool: {response}\n")

        # Now, use the OpenAI client with MCP tool integration
        client_openai = OpenAI()

        print("\n GPT-4o-mini Response with MCP tool integration:")
        resp = client_openai.responses.create(
            model= OPENAI_MODEL,
            tools=[
                {
                    "type": "mcp",
                    "server_label": "count_r_server",
                    "server_url": MCP_SERVER_URL,
                    "require_approval": "never",
                    "headers": {
                        "Authorization": f"Bearer {FASTMCP_API_KEY}"
                    }
                },
            ],
            input="Count the number of times the letter 'R' appears in the following text: 'Rapidly running rabbits rapidly run.'",
        )
        print(resp)

if __name__ == "__main__":
    asyncio.run(main())