import asyncio
from fastmcp import Client

async def main():
    async with Client("https://fiscal-bronze-tuna.fastmcp.app/mcp") as client:
        result = await client.call_tool(
            name="say_hello", 
            arguments={"name": "Pepito"}
        )
    print(result)

asyncio.run(main())