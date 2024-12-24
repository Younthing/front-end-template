from fastapi import Header, HTTPException
from typing import Annotated

async def get_token_header(x_token: Annotated[str, Header()]) -> str:
    """Simple header dependency for demonstration"""
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token