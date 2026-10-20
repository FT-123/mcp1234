import psutil
import asyncio
from typing import List, Dict
from config import TIMEOUT_SECONDS

async def list_processes() -> List[Dict[str, str]]:
    """List running processes."""
    processes = []
    try:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                processes.append({
                    "pid": str(proc.info['pid']),
                    "name": proc.info['name'],
                    "username": proc.info['username']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    except Exception as e:
        return [{"error": str(e)}]
    return processes

async def kill_process(pid: int) -> bool:
    """Terminate a process."""
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait(timeout=5)
        return True
    except Exception:
        return False