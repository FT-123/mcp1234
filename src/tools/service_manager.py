import subprocess
import asyncio
from typing import List, Dict
from config import TIMEOUT_SECONDS

async def list_services() -> List[Dict[str, str]]:
    """List Windows services."""
    try:
        # Run sc query to get services
        result = subprocess.run(
            ["sc", "query"],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=True
        )
        # Parse output (simplified)
        services = []
        for line in result.stdout.split('\n'):
            if 'SERVICE_NAME:' in line:
                service_name = line.split('SERVICE_NAME:')[1].strip()
                services.append({"name": service_name})
        return services
    except Exception as e:
        return [{"error": str(e)}]

async def start_service(service_name: str) -> bool:
    """Start a Windows service."""
    try:
        result = subprocess.run(
            ["sc", "start", service_name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=True
        )
        return True
    except Exception:
        return False

async def stop_service(service_name: str) -> bool:
    """Stop a Windows service."""
    try:
        result = subprocess.run(
            ["sc", "stop", service_name],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=True
        )
        return True
    except Exception:
        return False