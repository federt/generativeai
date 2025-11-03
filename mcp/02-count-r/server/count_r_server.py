import os
from fastmcp import FastMCP

# Use a stable server label that the client expects when requesting tools.
# The client uses server_label="count_r_server", so expose the same label here.
mcp = FastMCP("count_r_server")

@mcp.tool
def count_r(text: str) -> int:
    """Counts the occurrences of 'r' in the given text."""
    return text.lower().count('r')


if __name__ == "__main__":
    
    transport = os.environ.get("MCP_TRANSPORT", "http")
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", os.environ.get("PORT", 8000)))
    
    print(f"Starting FastMCP on {host}:{port}")
    mcp.run(transport=transport,host=host, port=port)
