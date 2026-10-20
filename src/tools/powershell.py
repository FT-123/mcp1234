import subprocess
import asyncio
from typing import Dict
from config import TIMEOUT_SECONDS, COMMAND_ALLOWLIST
import os

async def run_powershell(command: str) -> str:
    """Execute PowerShell command."""
    # Check if command is allowed
    if COMMAND_ALLOWLIST and command not in COMMAND_ALLOWLIST:
        return f"Command not in allowlist: {command}"
    
    try:
        # Execute PowerShell command
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=True
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return f"Command timed out after {TIMEOUT_SECONDS}s"
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"
    except Exception as e:
        return f"Error: {e}"