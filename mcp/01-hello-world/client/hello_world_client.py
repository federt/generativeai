import asyncio
import os
from fastmcp import Client

async def main():
    mcp_url = os.environ.get("MCP_URL", "http://localhost:8000/mcp")
    async with Client(mcp_url) as client:
        result = await client.call_tool(
            name="say_hello", 
            arguments={"name": "Jhon Doe"}
        )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())