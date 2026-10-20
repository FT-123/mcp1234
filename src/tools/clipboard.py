import pyperclip
import asyncio
from typing import Dict
from config import TIMEOUT_SECONDS

async def read_clipboard() -> str:
    """Read clipboard content."""
    try:
        content = pyperclip.paste()
        return content
    except Exception as e:
        return f"Error reading clipboard: {e}"

async def write_clipboard(text: str) -> bool:
    """Write text to clipboard."""
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        return False