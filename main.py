from fastmcp import FastMCP
import random

# Create the FastMCP server
mcp = FastMCP("Demo Server")


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
    mcp.run()
