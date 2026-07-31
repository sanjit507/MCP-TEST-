
import os
import random
from mcp.server.fastmcp import FastMCP

# Create the FastMCP server
mcp = FastMCP("Demo Server")

# Configure host and port for cloud deployment (e.g. Render)
port = int(os.environ.get("PORT", 8000))
mcp.settings.host = "0.0.0.0"
mcp.settings.port = port

# Allow connection from remote host domains (e.g. *.onrender.com)
if mcp.settings.transport_security:
    mcp.settings.transport_security.allowed_hosts = ["*"]
    mcp.settings.transport_security.allowed_origins = ["*"]


@mcp.tool()
def roll_dice(n_dice: int) -> list[int]:
    """
    Roll one or more six-sided dice.

    Args:
        n_dice: Number of dice to roll.

    Returns:
        A list of random dice values.
    """
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    # Use SSE (Server-Sent Events) transport for web/remote deployment
    mcp.run(transport="sse")

