import json
import time
from typing import Dict, Any
from config import AUDIT_LOG_PATH

def log_action(action: str, input_data: Dict[str, Any], result: Any, user: str = "unknown"):
    """Log action to audit log."""
    log_entry = {
        "timestamp": time.time(),
        "action": action,
        "input": input_data,
        "result": result,
        "user": user
    }
    
    try:
        with open(AUDIT_LOG_PATH, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception:
        # Silently fail to avoid breaking the system
        pass