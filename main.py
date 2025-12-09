from fastmcp import FastMCP
import json
import random 

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int, b: int) -> int:
    """
    Add Two Number Together.
    
    Args:
        a: First Number
        b: Second Number
        
    Returns:
        The Sum of A and B
    """
    
    return a + b

@mcp.tool
def random_number(min_value:int = 1, max_value:int =100) -> int:
    """Generate a random number within a range

    Args:
        min_value (int, optional): minimum value. Defaults to 1.
        max_value (int, optional): maximum value. Defaults to 100.

    Returns:
        int: a random integer between min_val and max_val
        
    """
    
    return random.randint(min_value, max_value)


@mcp.resource("info://server")
def server_info() -> str:
    """get information about this server

    Returns:
        str: information about this server
    """
    
    info = {
        "name" : "Simple Calculator server",
        "version" : "1.0.0",
        "description" : "A bsic mcp server with the math tool",
        "tools" : ["add", "random_number"],
        "author" : "Dhruv Panchal"
    }
    

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)