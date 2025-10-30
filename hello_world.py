from fastmcp import FastMCP

mcp = FastMCP("Hello_World 🚀")

@mcp.tool
def say_hello(name: str) -> str:
    """Says hello"""
    return f'Hello, {name}!'

if __name__ == "__main__":
    mcp.run()