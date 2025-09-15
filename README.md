# 🤖 Multi-Agent Assistant  

This repository contains a Python example demonstrating how to create a multi-agent assistant system using the Gemini API and the `agents` library. The system includes specialized agents for Medical and Computer Science assistance, with a main agent that can hand off tasks to these specialized agents.

## Features

- Uses Gemini API for language model completions.
- Defines multiple agents with specific roles:
  - Medical Assistant
  - Computing Assistant
  - Main Assistant that delegates tasks.
- Asynchronous execution with `asyncio`.
- Environment variable support for API keys and base URL.
- Easy to extend with additional agents and handoffs. 
 
## Requirements

- Python 3.8+
- `agents` library
- `python-dotenv` for environment variable loading
- Access to Gemini API with valid API key

## Setup

### 1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
### 2. Create a .env file in the root directory and add your Gemini API credentials:

  ```env

GEMINI_API_KEY=your_gemini_api_key_here
base_url=https://api.your-gemini-endpoint.com
  ```
### 3. Install dependencies:
  ```bash
pip install -r requirements.txt
  ```
## Usage
Run the main script to start the multi-agent assistant:
  ```bash
python main.py
  ```
## 👨‍💻 Author
Kaif Shamim Crafted with curiosity and code.




