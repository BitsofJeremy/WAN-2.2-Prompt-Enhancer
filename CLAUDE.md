# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WAN 2.2 Prompt Enhancer is a professional Python CLI tool that transforms basic prompts into cinematic video generation prompts using Google's Gemini AI. It implements the WAN 2.2 aesthetic control system with modern Python packaging and uv single-file script support for easy distribution.

## Architecture

### Core Components

- **`wan_prompt_enhancer.py`** - Main application as uv single-file script:
  - Inline dependency declaration using `# /// script` format
  - `PromptEnhancer` class - Fully typed wrapper around Gemini API
  - `SYSTEM_PROMPT` - Comprehensive WAN 2.2 prompt engineering instructions
  - Modern CLI with argparse, enhanced error messages, and interactive mode

- **`pyproject.toml`** - Modern Python packaging configuration:
  - Hatchling build system
  - Development dependencies (black, isort, flake8, mypy, pytest)
  - Tool configurations for code quality
  - Entry point script definition

### WAN 2.2 System Implementation
Implements Advanced Formula: **Subject + Scene + Motion + Aesthetic Control + Stylization**

Key architectural elements:
- Comprehensive type hints throughout codebase
- Professional error handling with user-friendly messages  
- Interactive mode with session tracking and enhanced UX
- Environment variable and CLI argument API key management

## Development Commands

### Setup and Installation

**Recommended (uv):**
```bash
# No setup required - run directly with uv
uv run wan_prompt_enhancer.py "your prompt"

# Clone for development
git clone <repo-url>
cd WAN-2.2-Prompt-Enhancer
uv sync --dev
```

**Traditional:**
```bash
# Install with pip
pip install -e ".[dev]"

# Or just dependencies
pip install google-genai
```

### Running the Application

**uv single-file script (recommended):**
```bash
# Direct execution
uv run wan_prompt_enhancer.py "prompt text"
uv run wan_prompt_enhancer.py --interactive

# With API key
uv run wan_prompt_enhancer.py "prompt" --api-key YOUR_KEY
```

**Traditional execution:**
```bash
python wan_prompt_enhancer.py "prompt text"
python wan_prompt_enhancer.py --interactive
```

### Code Quality and Development

```bash
# Format code
black .
isort .

# Lint and type check
flake8 .
mypy .

# Run tests (when implemented)
pytest
pytest --cov
```

## API Integration

### Gemini Configuration
- Uses `google-genai>=0.8.0` library
- Model: `gemini-2.5-flash` for optimal speed/quality balance
- Thinking budget: 0 for faster response times
- Robust error handling with informative user messages

### Authentication Methods
1. Environment variable: `GEMINI_API_KEY`
2. CLI argument: `--api-key`
3. Interactive prompting with clear instructions

## Code Quality Standards

### Type Hints
- Complete type annotations throughout codebase
- Uses `Optional[str]` for nullable parameters
- Return types specified for all functions
- Mypy configuration enforces strict typing

### Error Handling
- Graceful API failure handling
- User-friendly error messages with emojis
- Comprehensive input validation
- Keyboard interrupt handling in interactive mode

### CLI Design
- Professional help text with examples
- Version information
- Enhanced interactive mode with session tracking
- Clear progress indicators and user feedback

## File Structure

```
WAN-2.2-Prompt-Enhancer/
├── wan_prompt_enhancer.py    # Main uv script with inline deps
├── pyproject.toml           # Modern Python packaging config
├── README.md               # Comprehensive documentation
├── CLAUDE.md              # This file
├── LICENSE                # AGPL-3.0
└── .gitignore            # Python + uv gitignore
```

## Dependencies and Packaging

### Runtime Dependencies
- `google-genai>=0.8.0` - Google Gemini AI client

### Development Dependencies
- `black>=23.0.0` - Code formatting
- `isort>=5.12.0` - Import sorting
- `flake8>=6.0.0` - Code linting
- `mypy>=1.0.0` - Static type checking
- `pytest>=7.0.0` - Testing framework
- `pytest-cov>=4.0.0` - Coverage reporting

### Packaging Features
- uv single-file script with inline dependencies
- Modern pyproject.toml configuration
- Entry point script: `wan-enhancer`
- Cross-platform compatibility (Python 3.9+)

## Testing and Validation

When implementing tests:
```bash
# Test structure
tests/
├── conftest.py              # Test fixtures
├── test_prompt_enhancer.py  # Unit tests for PromptEnhancer class
├── test_cli.py             # CLI interface tests
└── test_integration.py     # Integration tests with Gemini API
```

## Usage Patterns

### Single Prompt Enhancement
```python
enhancer = PromptEnhancer(api_key="key")
result = enhancer.enhance_prompt("dragon flying")
```

### Interactive Session
- Session tracking with prompt counter
- Enhanced UX with progress indicators
- Graceful exit handling

## Reference Documentation

- WAN 2.2 Guide: https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
- Google Gemini API: https://ai.google.dev/
- uv Documentation: https://docs.astral.sh/uv/