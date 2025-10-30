import asyncio
from fastmcp import Client

async def main():
    async with Client("hello_world.py") as client:
        result = await client.call_tool(
            name="say_hello", 
            arguments={"name": "Homer"}
        )
    print(result)

asyncio.run(main())