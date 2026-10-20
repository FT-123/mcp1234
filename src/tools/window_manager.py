import win32gui
import win32process
from typing import List, Dict
from config import TIMEOUT_SECONDS
import asyncio

async def list_windows() -> List[Dict[str, str]]:
    """List all visible windows."""
    windows = []
    
    def enum_windows_callback(hwnd, windows_list):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:  # Only include windows with titles
                windows_list.append({
                    "id": str(hwnd),
                    "title": window_title,
                    "class": win32gui.GetClassName(hwnd),
                    "pid": pid
                })
        return True
    
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

async def get_active_window() -> Dict[str, str]:
    """Get the currently focused window."""
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        return {
            "id": str(hwnd),
            "title": win32gui.GetWindowText(hwnd),
            "class": win32gui.GetClassName(hwnd)
        }
    return {"id": "", "title": "", "class": ""}

async def focus_window(window_id: str) -> bool:
    """Bring a window to the foreground."""
    hwnd = int(window_id)
    try:
        # Bring window to foreground
        win32gui.SetForegroundWindow(hwnd)
        # Give it a moment to focus
        await asyncio.sleep(0.1)
        return True
    except Exception:
        return False