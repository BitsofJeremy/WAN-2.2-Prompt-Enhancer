# 🎬 WAN 2.2 Prompt Enhancer

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Turn your simple ideas into Hollywood-quality video prompts! This tool takes basic descriptions like "a cat playing piano" and transforms them into professional, cinematic prompts perfect for AI video generation tools.

## What This Does

**Input:** `a dragon flying over mountains`

**Output:** 
```
1. **Epic Fantasy Cinematography**, golden hour lighting, wide-angle aerial shot, 
   warm amber and crimson color palette. A majestic dragon with iridescent scales 
   soars gracefully above snow-capped mountain peaks...

2. **Dark Cinematic Style**, stormy overcast lighting, low-angle perspective,
   cool blue and steel color grading. A powerful dragon cuts through heavy storm 
   clouds above jagged mountain ridges...

[Plus 3 more unique cinematic variations]
```

## ⚡ Quick Start (2 Steps)

### Step 1: Get a Google AI API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key" 
3. Copy your key (starts with `AIza...`)

### Step 2: Set Up Configuration

**Option A: Using .env file (Recommended)**
```bash
# Download the example configuration
wget https://raw.githubusercontent.com/BitsofJeremy/WAN-2.2-Prompt-Enhancer/main/.env-example

# Copy to .env and edit with your API key
cp .env-example .env
# Edit .env and add your GEMINI_API_KEY

# Run it! (No other setup needed)
uv run wan_prompt_enhancer.py "a robot dancing in the rain"
```

**Option B: Environment Variable**
```bash
# Set your API key
export GEMINI_API_KEY="your-api-key-here"

# Run it!
uv run wan_prompt_enhancer.py "a robot dancing in the rain"
```

**Option C: Command Line**
```bash
# Pass API key directly
uv run wan_prompt_enhancer.py "your prompt" --api-key "your-key-here"
```

## 🎮 How to Use

### Basic Usage
```bash
# Single prompt (replace with your idea)
uv run wan_prompt_enhancer.py "a wizard casting spells"

# Interactive mode (keep entering prompts)
uv run wan_prompt_enhancer.py --interactive

# Or pass API key directly if not using .env file
uv run wan_prompt_enhancer.py "your prompt" --api-key "your-key"

# Use a different model
uv run wan_prompt_enhancer.py "your prompt" --model "gemini-1.5-pro"
```

### Download and Use Locally
```bash
# Download the script
wget https://raw.githubusercontent.com/BitsofJeremy/WAN-2.2-Prompt-Enhancer/main/wan_prompt_enhancer.py

# Run it
uv run wan_prompt_enhancer.py "a spaceship landing"
```

## 🎭 More Examples

| Simple Input | Professional Output Style |
|-------------|----------------------------|
| `cat playing piano` | **Whimsical Studio Setup**, soft key lighting, medium close-up... |
| `storm over ocean` | **Epic Natural Drama**, overcast lighting, wide-angle shot... |
| `robot in city` | **Sci-Fi Urban**, neon lighting, low-angle perspective... |
| `sunset on beach` | **Romantic Cinematography**, golden hour, tracking shot... |

## 🔧 Interactive Mode Demo

```bash
$ uv run wan_prompt_enhancer.py --interactive

🎬 WAN 2.2 Prompt Enhancer - Interactive Mode
💡 Tips: Be descriptive but concise

📝 Enter your basic prompt: magical forest
🎯 Enhancing: 'magical forest'
✨ Generating cinematic variations...
============================================================
1. **Fantasy Adventure Style**, dappled sunlight filtering through ancient trees...
2. **Mystical Atmosphere**, ethereal mist, low-angle shot revealing towering oaks...
[Plus 3 more variations]
============================================================
✅ Enhanced prompt #1. Ready for your next prompt!

📝 Enter your basic prompt: quit
👋 Thanks for using WAN 2.2 Prompt Enhancer! Enhanced 1 prompts.
```

## ⚙️ Configuration Options

### .env File Settings
```bash
# Your Google Gemini API key (required)
GEMINI_API_KEY=your-api-key-here

# Model to use (optional, default: gemini-2.5-flash)
GEMINI_MODEL=gemini-2.5-flash

# Thinking budget for more deliberate responses (optional, default: 0)
GEMINI_THINKING_BUDGET=0
```
