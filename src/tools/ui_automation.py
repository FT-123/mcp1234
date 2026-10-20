import uiautomation as auto
import asyncio
from typing import Dict, Optional, Any
from config import TIMEOUT_SECONDS
import time

async def get_ui_tree(window_id: str) -> Dict[str, Any]:
    """Get the UI Automation tree for a window."""
    hwnd = int(window_id)
    try:
        # Get the window element
        window = auto.WindowControl(searchDepth=0, searchFromControl=auto.GetRootControl())
        window = window.FindWindow(searchDepth=0, searchFromControl=auto.GetRootControl())
        # Get UI tree
        tree = _element_to_dict(window)
        return tree
    except Exception as e:
        return {"error": str(e)}

async def find_ui_element(window_id: str, criteria: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Find a UI element by criteria."""
    hwnd = int(window_id)
    try:
        # Get the window element
        window = auto.WindowControl(searchDepth=0, searchFromControl=auto.GetRootControl())
        # Search for element
        element = window.FindControl(
            searchDepth=10,
            searchFromControl=auto.GetRootControl(),
            searchCriteria=criteria
        )
        if element:
            return {
                "id": str(element.NativeWindowHandle),
                "name": element.Name,
                "control_type": element.ControlTypeName
            }
        return None
    except Exception as e:
        return {"error": str(e)}

async def click_element(element_id: str) -> bool:
    """Click a UI element."""
    try:
        hwnd = int(element_id)
        element = auto.ControlFromHandle(hwnd)
        if element:
            element.Click()
            return True
        return False
    except Exception:
        return False

async def type_text(text: str) -> bool:
    """Type text into a focused element."""
    try:
        auto.SendKeys(text)
        return True
    except Exception:
        return False

async def send_keys(keys: str) -> bool:
    """Send keyboard shortcuts."""
    try:
        auto.SendKeys(keys)
        return True
    except Exception:
        return False

def _element_to_dict(element: auto.Control) -> Dict[str, Any]:
    """Convert UI element to dictionary."""
    return {
        "name": element.Name,
        "control_type": element.ControlTypeName,
        "id": str(element.NativeWindowHandle),
        "children": [
            _element_to_dict(child) for child in element.GetChildren()
        ]
    }