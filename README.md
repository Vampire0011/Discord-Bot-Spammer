# Discord Random Number Sender

A Python project that demonstrates generating random numeric strings and sending HTTP requests to Discord.

> **Important:** The supplied `main.py` repeatedly sends messages to a Discord channel. Do not use it to spam, harass, or disrupt a server, and do not run it in a channel without the server owner's explicit permission. Discord may rate-limit or restrict accounts that automate unwanted messages.

## Features

- Generates random numeric strings with a configurable length.
- Uses Python's `requests` library to make HTTP requests.
- Includes a configurable delay between requests.
- Prints basic information about request failures and rate limits.

## Requirements

- Python 3.10 or newer
- Git
- Internet connection
- The `requests` Python package

## 1. Install Python

Download Python from [python.org/downloads](https://www.python.org/downloads/).

On Windows, enable **Add Python to PATH** during installation.

Check that Python and pip are available:

```bash
python --version
python -m pip --version
```

If your system uses `python3`, use that command instead of `python`.

## 2. Clone the repository

Replace `YOUR_USERNAME/YOUR_REPOSITORY` with the actual GitHub repository path:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

If you have downloaded the project as a ZIP instead, extract it and open a terminal in the extracted folder.

## 3. Create a virtual environment (recommended)

**Windows — PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows — Command Prompt:**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install the required library

The script imports `requests`. The other imported modules (`time`, `random`, `sys`, and `os`) are included with Python.

```bash
python -m pip install --upgrade pip
python -m pip install requests
```

To record the dependency for a project environment:

```bash
python -m pip freeze > requirements.txt
```

## 5. Review the code before running

The current script contains an embedded credential and an infinite sending loop. **Do not run the uploaded version as-is.**

- Revoke/rotate the exposed Discord token immediately if it was real.
- Never commit tokens, passwords, or other credentials to Git.
- Do not use a personal account token for automation.
- For a legitimate integration, use an official Discord bot/application and supported API/library methods.
- Test message-generation logic locally first, without sending network requests.
- Add an explicit stop condition, permission checks, and conservative rate limits before any authorized integration test.

## 6. Run a local-only check

You can check that Python can parse the file without executing its message-sending loop:

```bash
python -m py_compile main.py
```

This checks syntax only; it does not run the program or verify Discord access.

## Troubleshooting

### `ModuleNotFoundError: No module named 'requests'`

Install the dependency in the active environment:

```bash
python -m pip install requests
```

### `python` is not recognized

Reinstall Python with **Add Python to PATH** enabled, or try `py --version` on Windows.

### HTTP 401 / invalid credentials

Do not paste credentials into an issue, chat, screenshot, or public repository. Revoke exposed credentials and configure a new credential securely for an authorized application.

### HTTP 429 / rate limited

The API is limiting requests. Do not try to bypass rate limits; stop the test and follow the platform's published limits and retry guidance.

## Project structure

```text
YOUR_REPOSITORY/
├── main.py
├── README.md
└── requirements.txt   # optional; create this if needed
```

## Responsible use

Use this project only for authorized learning and testing. Avoid unsolicited messages, repeated posts, and activity that disrupts other users. For a real Discord integration, consult the [Discord Developer Documentation](https://discord.com/developers/docs/).

## License

No license is specified. Add a license file if you intend to publish or share this project.
