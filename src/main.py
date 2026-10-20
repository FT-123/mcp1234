import asyncio
import sys
from fastmcp import MCP, Tool
from tools.window_manager import list_windows, get_active_window, focus_window
from tools.ui_automation import get_ui_tree, find_ui_element, click_element, type_text, send_keys
from tools.clipboard import read_clipboard, write_clipboard
from tools.process_manager import list_processes, kill_process
from tools.powershell import run_powershell
from tools.service_manager import list_services, start_service, stop_service
from tools.file_io import read_file, write_file, list_dir
from security.validation import validate_input
from transport.stdio import setup_stdio_transport

# Initialize MCP server
mcp = MCP()

# Register tools
mcp.register_tool(Tool("list_windows", list_windows))
mcp.register_tool(Tool("get_active_window", get_active_window))
mcp.register_tool(Tool("focus_window", focus_window))
mcp.register_tool(Tool("get_ui_tree", get_ui_tree))
mcp.register_tool(Tool("find_ui_element", find_ui_element))
mcp.register_tool(Tool("click_element", click_element))
mcp.register_tool(Tool("type_text", type_text))
mcp.register_tool(Tool("send_keys", send_keys))
mcp.register_tool(Tool("screenshot", screenshot))
mcp.register_tool(Tool("read_clipboard", read_clipboard))
mcp.register_tool(Tool("write_clipboard", write_clipboard))
mcp.register_tool(Tool("list_processes", list_processes))
mcp.register_tool(Tool("kill_process", kill_process))
mcp.register_tool(Tool("run_powershell", run_powershell))
mcp.register_tool(Tool("list_services", list_services))
mcp.register_tool(Tool("start_service", start_service))
mcp.register_tool(Tool("stop_service", stop_service))
mcp.register_tool(Tool("read_file", read_file))
mcp.register_tool(Tool("write_file", write_file))
mcp.register_tool(Tool("list_dir", list_dir))

# Setup transport
setup_stdio_transport(mcp)

if __name__ == "__main__":
    asyncio.run(mcp.start())