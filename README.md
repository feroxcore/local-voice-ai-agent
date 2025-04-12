# Local Voice AI Agent

A real-time voice chat application powered by local AI models. This project allows you to have voice conversations with AI models like Gemma running locally on your machine.

## Features

- Real-time speech-to-text conversion
- Local LLM inference using Ollama
- Text-to-speech response generation
- Web interface for interaction
- Phone number interface option

## Prerequisites

- MacOS
- [Ollama](https://ollama.ai/) - Run LLMs locally
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Installation

### 1. Install prerequisites with Homebrew

```bash
brew install ollama
brew install uv
```

### 2. Clone the repository

```bash
git clone https://github.com/jesuscopado/local-voice-ai-agent.git
cd local-voice-ai-agent
```

### 3. Set up Python environment and install dependencies

```bash
uv venv
source .venv/bin/activate
uv sync
```

### 4. Download required models in Ollama

```bash
ollama pull gemma3:1b
# For advanced version
ollama pull gemma3:4b
```

## Usage

### Basic Voice Chat

```bash
python local_voice_chat.py
```

### Advanced Voice Chat (with system prompt)

#### Web UI (default)
```bash
python local_voice_chat_advanced.py
```

#### Phone Number Interface
Get a temporary phone number that anyone can call to interact with your AI:
```bash
python local_voice_chat_advanced.py --phone
```

This will provide you with a temporary phone number that you can call to interact with the AI using your voice.

## How it works

The application uses:
- `FastRTC` for WebRTC communication
- `Moonshine` for local speech-to-text conversion
- `Kokoro` for text-to-speech synthesis
- `Ollama` for running local LLM inference with `Gemma` models

When you speak, your audio is:
1. Transcribed to text using Moonshine
2. Sent to a local LLM via Ollama for processing
3. The LLM response is converted back to speech with Kokoro
4. The audio response is streamed back to you via FastRTC
