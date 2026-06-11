# LLM Tools Lab

A project that gives an LLM access to real-world tools using AISuite.

## What it does
The LLM can use 4 tools to take real actions in the world:
- 🕐 **Get Current Time** - Returns the current time
- 🌤 **Get Weather** - Gets real weather for your location
- 📝 **Write Text File** - Creates real files on your computer
- 📱 **Generate QR Code** - Creates real scannable QR codes

## How it works
1. You give the LLM a question in plain English
2. LLM decides which tool to use
3. AISuite runs the tool automatically
4. LLM gives you the final answer

## Setup

### Install dependencies
pip install aisuite openai python-dotenv qrcode pillow requests


### Add your API key
Create a `.env` file and add:
OPENAI_API_KEY=your_openai_key_here


### Run
python3 main.py


## What I learned
- How LLMs call tools behind the scenes
- How AISuite automates tool calling
- How LLM picks the right tool automatically
- How LLM can use multiple tools together
