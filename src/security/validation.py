from typing import Dict, Any
from config import PATH_ALLOWLIST, COMMAND_ALLOWLIST
import os

def validate_input(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate input data."""
    # Check for dangerous inputs
    if "path" in input_data and PATH_ALLOWLIST:
        if input_data["path"] not in PATH_ALLOWLIST:
            return {"error": "Path not in allowlist"}
    
    if "command" in input_data and COMMAND_ALLOWLIST:
        if input_data["command"] not in COMMAND_ALLOWLIST:
            return {"error": "Command not in allowlist"}
    
    # Check for path traversal
    if "path" in input_data:
        path = input_data["path"]
        if ".." in path or path.startswith("/") or path.startswith("\\"):
            return {"error": "Path traversal detected"}
    
    return {"valid": True}