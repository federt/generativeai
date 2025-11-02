import os
from fastmcp import FastMCP


mcp = FastMCP("Hello_World 🚀")


@mcp.tool
def say_hello(name: str) -> str:
    """Says hello"""
    return f'Hello, {name} !'


if __name__ == "__main__":
    
    transport = os.environ.get("MCP_TRANSPORT", "http")
    # Allow overriding host/port via env vars for containerization
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    # Support common PORT var and custom MCP_PORT
    port = int(os.environ.get("MCP_PORT", os.environ.get("PORT", 8000)))
    print(f"Starting FastMCP on {host}:{port}")
    mcp.run(transport=transport,host=host, port=port)
