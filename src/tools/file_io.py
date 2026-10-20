import os
import asyncio
from typing import List, Dict
from config import TIMEOUT_SECONDS, PATH_ALLOWLIST
import hashlib

async def read_file(path: str) -> str:
    """Read a file."""
    # Check if path is allowed
    if PATH_ALLOWLIST and path not in PATH_ALLOWLIST:
        return f"Path not in allowlist: {path}"
    
    try:
        with open(path, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"

async def write_file(path: str, content: str) -> bool:
    """Write to a file."""
    # Check if path is allowed
    if PATH_ALLOWLIST and path not in PATH_ALLOWLIST:
        return False
    
    try:
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception:
        return False

async def list_dir(path: str) -> List[str]:
    """List directory contents."""
    # Check if path is allowed
    if PATH_ALLOWLIST and path not in PATH_ALLOWLIST:
        return [f"Path not in allowlist: {path}"]
    
    try:
        contents = os.listdir(path)
        return contents
    except Exception as e:
        return [f"Error listing directory: {e}"]