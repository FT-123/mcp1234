import os
from typing import List, Optional

# Environment-based configuration
ENABLE_DANGEROUS_TOOLS = os.getenv("ENABLE_DANGEROUS_TOOLS", "false").lower() == "true"
AUDIT_LOG_PATH = os.getenv("AUDIT_LOG_PATH", "audit.log")
TIMEOUT_SECONDS = float(os.getenv("TIMEOUT_SECONDS", "5.0"))

# Allowlists
PATH_ALLOWLIST: Optional[List[str]] = (
    os.getenv("PATH_ALLOWLIST", "").split(",") if os.getenv("PATH_ALLOWLIST") else None
)
COMMAND_ALLOWLIST: Optional[List[str]] = (
    os.getenv("COMMAND_ALLOWLIST", "").split(",") if os.getenv("COMMAND_ALLOWLIST") else None
)

# Security settings
CONFIRMATION_TOKEN = os.getenv("CONFIRMATION_TOKEN", "")

# Transport settings
USE_HTTP = os.getenv("USE_HTTP", "false").lower() == "true"
HTTP_PORT = int(os.getenv("HTTP_PORT", "8080"))