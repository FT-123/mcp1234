# MCP Server for Windows AI Agent Control

## Architecture Summary

The MCP server is a Python-based service that exposes a structured API for controlling Windows. It operates as a local stdio server, with optional HTTP/SSE transport. The architecture consists of:

1. **MCP Tool Layer**: Exposes commands like `list_windows`, `click_element`, `run_powershell`, etc., validated and secured before execution.
2. **Windows Control Layer**: Uses UI Automation (UIA) and structured tools (e.g., pywinauto, psutil) to interact with the OS.
3. **Validation & Security Layer**: Enforces path allowlists, command restrictions, and requires confirmation for dangerous actions.
4. **Logging Layer**: Audits all tool invocations and errors to a structured log.

The server is configured via environment variables for security, timeouts, and allowlists. All tools have explicit risk levels and safe defaults. Errors are handled with timeouts and output limits to prevent hangs. PowerShell is executed via `shell_execute` with `shell=False` to prevent injection.

## 1. MVP Scope and Non-Goals

**In v1**: Basic UI Automation (list_windows, get_active_window, focus_window, get_ui_tree, find_ui_element, click_element, type_text, send_keys), screenshot, clipboard, process control (list_processes, kill_process), PowerShell execution (run_powershell), service control (list_services, start_service, stop_service), file system (read_file, write_file, list_dir).

**Deferred**: Registry, OCR, pixel-based clicks, HTTP/SSE transport, advanced PowerShell, path traversal, complex input handling.

## 2. Architecture

- **Layers**: MCP Tool -> Windows Control -> Validation/Security -> Logging.
- **Transport**: stdio (default), optional HTTP/SSE.
- **Configuration**: Environment variables for security, timeouts, allowlists.
- **Error Handling**: All tools have timeouts and output limits; errors are logged and returned to the client.

## 3. MVP MCP Tool List

| Tool Name | Purpose | Input Schema | Return Shape | Risk Level | Safe Default | Limits/Timeouts |
|---|---|---|---|---|---|---|
| list_windows | List all open windows | None | List of window objects (title, handle, class) | Low | Enabled | None |
| get_active_window | Get the active window | None | Window object | Low | Enabled | None |
| focus_window | Focus a window | window_handle | Boolean | Low | Enabled | None |
| get_ui_tree | Get UI tree for a window | window_handle | UI tree (element hierarchy) | Low | Enabled | None |
| find_ui_element | Find an element by properties | window_handle, properties | Element object | Low | Enabled | None |
| click_element | Click an element | element_handle | Boolean | Low | Enabled | None |
| type_text | Type text into an element | element_handle, text | Boolean | Low | Enabled | None |
| send_keys | Send keys to an element | element_handle, keys | Boolean | Low | Enabled | None |
| screenshot | Take a screenshot | window_handle | Image file path | Low | Enabled | None |
| read_clipboard | Read clipboard | None | String | Low | Enabled | None |
| write_clipboard | Write to clipboard | text | Boolean | Low | Enabled | None |
| list_processes | List all processes | None | List of process objects | Low | Enabled | None |
| kill_process | Kill a process | process_handle | Boolean | Low | Enabled | None |
| run_powershell | Run a PowerShell command | command | Output | Low | Enabled | None |
| list_services | List all services | None | List of service objects | Low | Enabled | None |
| start_service | Start a service | service_name | Boolean | Low | Enabled | None |
| stop_service | Stop a service | service_name | Boolean | Low | Enabled | None |
| read_file | Read a file | file_path | String | Low | Enabled | None |
| write_file | Write to a file | file_path, content | Boolean | Low | Enabled | None |
| list_dir | List a directory | directory_path | List of file objects | Low | Enabled | None |

## 4. Security Model

- **Dangerous Tools**: None in MVP; all tools are safe. Future tools like `kill_process` or `run_powershell` will be audited for risks.
- **Allowlists**: Path allowlists for file system tools; command allowlists for PowerShell.
- **Confirmation**: No confirmation needed for MVP; all tools are safe.
- **Audit Log**: Logs all tool invocations, errors, and outputs to a structured log file.
- **Timeouts**: All tools have timeouts to prevent hangs.
- **Protection**: PowerShell is executed via `shell_execute` with `shell=False` to prevent injection; path traversal is prevented by allowlists.

## 5. Dependencies

- **UI Automation**: pywinauto (for UIA and window control)
- **Process Control**: psutil (for process management)
- **Screenshot**: mss (for screen capture) + Pillow (for image processing)
- **Clipboard**: pyperclip (for clipboard operations)
- **Validation**: pydantic (for input validation)
- **Testing**: pytest (for unit and integration tests)

## 6. Project Structure

```
src/
├── main.py
├── tools/
│   ├── __init__.py
│   ├── ui.py
│   ├── file.py
│   └── process.py
├── config/
│   └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_ui.py
│   └── test_file.py
└── requirements.txt
```

## 7. Test Strategy

- **Unit Tests**: Validate tool inputs, outputs, and error handling.
- **Integration Tests**: Test Windows interaction with mocked UIA (e.g., using pywinauto's mock capabilities).
- **Windows Only**: All integration tests are marked `windows_only`.

## 8. Implementation Milestones

1. **Milestone 1**: Implement core tools (UIA, file, process, service, clipboard).
2. **Milestone 2**: Add PowerShell execution and screenshot.
3. **Milestone 3**: Implement security (allowlists, audit logs) and testing.

## 9. Risks, Non-Obvious Issues, and Open Questions

- **UIA Reliability**: Windows UI Automation can be unreliable in some scenarios.
- **Path Traversal**: How to handle path traversal in file system tools.
- **PowerShell Injection**: How to prevent PowerShell injection.
- **Timeouts**: How to set appropriate timeouts for different tools.
- **Testing**: How to mock UIA for testing.

## Clarifying Questions

1. Should the MCP server support HTTP/SSE transport?
2. Should the MCP server support OCR and pixel-based clicks?
3. Should the MCP server support registry control?
4. Should the MCP server support advanced PowerShell execution?
5. Should the MCP server support complex input handling?
```