#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "google-genai>=0.8.0",
#     "python-dotenv>=1.0.0"
# ]
# ///
"""
WAN 2.2 Prompt Enhancer

A command-line tool that transforms basic prompts into cinematic, professional video generation prompts
using the WAN 2.2 aesthetic control system and Google's Gemini AI.

This tool implements the WAN 2.2 Advanced Formula: Subject + Scene + Motion + Aesthetic Control + Stylization
to create professional-grade video generation prompts from simple user inputs.

Example Usage:
    $ python wan_prompt_enhancer.py "a dragon flying over mountains"
    $ python wan_prompt_enhancer.py --interactive
    $ uv run wan_prompt_enhancer.py "dancing in the rain" --api-key YOUR_KEY

Author: Jeremy Schroeder
License: AGPL-3.0
"""

import argparse
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# System prompt for Gemini based on WAN 2.2 guide
# This comprehensive prompt teaches the AI to follow WAN 2.2's Advanced Formula
SYSTEM_PROMPT: str = """You are an expert cinematographer and prompt engineer specializing in WAN 2.2 video generation. Your job is to transform basic user inputs into professional, cinematic prompts that follow the WAN 2.2 aesthetic control system.

**Core Guidelines:**
- Use the Advanced Formula: Subject + Scene + Motion + Aesthetic Control + Stylization
- Always include specific technical terms from the WAN 2.2 guide
- Focus on cinematic storytelling with professional visual language
- Include lighting, camera angles, composition, and color grading
- Add motion descriptions and stylistic elements

**Required Elements to Include:**
1. **Aesthetic Control**: Light source, lighting type, time of day, shot size, composition, lens, color tone
2. **Camera Movement**: Basic or advanced camera movements when appropriate
3. **Stylization**: Visual style and/or visual effects
4. **Motion Description**: Specific, fluid motion details
5. **Technical Specifications**: Use exact terminology from the guide

**Format Instructions:**
- Use clean text without markdown formatting
- Include specific lighting setup and camera specifications
- Use professional cinematography vocabulary
- Make prompts vivid and detailed but not overly long
- Ensure prompts are optimized for video generation quality

**Example Transformations:**
Input: "a felt gnome village in the woods"
Output: "Felt style, golden hour sunlight, soft lighting, medium wide-angle, low-angle perspective, warm color palette. A whimsical village is nestled at the base of a giant, hollow tree trunk, surrounded by lush greenery and mushrooms. Little felt gnomes in woolen hats drive a miniature wooden train on moss-covered tracks. The train, pulled by tiny engine, transports acorns and berries in small carts. Sunlight filters through the leaves above, casting soft shadows and highlighting the rich textures of the bark and foliage."

Generate 3-5 enhanced prompt variations for each user input, each with different cinematic approaches but maintaining the core concept. Use diverse lighting, camera angles, and stylistic choices across variations. Format output as clean text without bold, italics, or other markdown formatting."""

class PromptEnhancer:
    """Main class for enhancing basic prompts into WAN 2.2 cinematic video prompts.
    
    This class wraps Google's Gemini AI API to transform simple user prompts into
    professional video generation prompts following the WAN 2.2 aesthetic control system.
    
    Attributes:
        client: Google Gemini AI client instance
    
    Example:
        >>> enhancer = PromptEnhancer(api_key="your_key_here")
        >>> enhanced = enhancer.enhance_prompt("a cat playing piano")
        >>> print(enhanced)
    """
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None) -> None:
        """Initialize the prompt enhancer with Gemini client.
        
        Args:
            api_key: Optional Gemini API key. If not provided, will use GEMINI_API_KEY
                    environment variable.
            model: Optional model name. If not provided, will use GEMINI_MODEL environment
                  variable or default to 'gemini-2.5-flash'.
                    
        Raises:
            SystemExit: If API key is not found or client initialization fails.
        """
        try:
            # Use provided API key or fall back to environment variable
            effective_api_key = api_key or os.getenv("GEMINI_API_KEY")
            
            if not effective_api_key:
                print("❌ Error: No API key found.")
                print("Please set GEMINI_API_KEY in .env file or use --api-key argument.")
                print("\nGet your API key at: https://makersuite.google.com/app/apikey")
                print("💡 Tip: Copy .env-example to .env and add your key")
                sys.exit(1)
                
            # Configure model (with fallback to environment variable or default)
            self.model = model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
            self.thinking_budget = int(os.getenv("GEMINI_THINKING_BUDGET", "0"))
                
            self.client = genai.Client(api_key=effective_api_key)
            
        except Exception as e:
            print(f"❌ Error initializing Gemini client: {e}")
            print("Please check your API key and internet connection.")
            sys.exit(1)

    def enhance_prompt(self, basic_prompt: str) -> str:
        """Transform a basic prompt into 3-5 enhanced WAN 2.2 style prompts.
        
        Takes a simple user prompt and generates multiple professional video generation
        prompts following the WAN 2.2 aesthetic control system. Each variation includes
        different cinematic approaches while maintaining the core concept.
        
        Args:
            basic_prompt: The basic prompt to enhance (e.g., "a cat playing piano")
            
        Returns:
            A formatted string containing 3-5 enhanced prompt variations, each with
            different lighting, camera angles, color palettes, and stylistic approaches.
            
        Example:
            >>> enhancer.enhance_prompt("a dragon flying")
            '1. **Epic Fantasy Style**, golden hour lighting, wide-angle shot...
             2. **Dark Cinematic Style**, stormy lighting, close-up shot...'
        """
        if not basic_prompt or not basic_prompt.strip():
            return "❌ Error: Please provide a valid prompt to enhance."
            
        try:
            user_request = f"""Transform this basic prompt into 3-5 professional WAN 2.2 video generation prompts with different cinematic approaches:

"{basic_prompt.strip()}"

Each variation should have different:
- Lighting setups (sunny, overcast, artificial, etc.)
- Camera angles and shot sizes
- Color palettes and moods  
- Stylistic approaches
- Motion descriptions

Number each variation (1-5) and ensure they're all visually distinct while maintaining the core concept."""

            # Create the full prompt by combining system and user prompts
            full_prompt = f"{SYSTEM_PROMPT}\n\nUser Request: {user_request}"
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=self.thinking_budget)
                )
            )
            
            return response.text
            
        except Exception as e:
            return f"❌ Error generating enhanced prompts: {e}\nPlease check your API key and internet connection."

def main() -> None:
    """Main entry point for the WAN 2.2 Prompt Enhancer CLI application.
    
    Handles command-line argument parsing and orchestrates the prompt enhancement
    workflow in either single-prompt or interactive mode.
    """
    parser = argparse.ArgumentParser(
        prog="wan-enhancer",
        description="🎬 Transform basic prompts into professional WAN 2.2 video generation prompts using AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🚀 Examples:
  python wan_prompt_enhancer.py "a dragon flying over mountains"
  python wan_prompt_enhancer.py "dancing in the rain" --api-key YOUR_KEY
  python wan_prompt_enhancer.py --interactive
  
  # With uv (recommended):
  uv run wan_prompt_enhancer.py "mystical forest scene"
  uv run wan_prompt_enhancer.py --interactive
  
📚 Get your Gemini API key at: https://makersuite.google.com/app/apikey
🔗 WAN 2.2 Guide: https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
        """
    )
    
    parser.add_argument(
        "prompt", 
        nargs="?", 
        help="Basic prompt to enhance into WAN 2.2 style (or use --interactive)",
        metavar="PROMPT"
    )
    
    parser.add_argument(
        "--api-key",
        help="Gemini API key (alternatively set GEMINI_API_KEY in .env file)",
        metavar="KEY"
    )
    
    parser.add_argument(
        "--model",
        help="Gemini model to use (alternatively set GEMINI_MODEL in .env file)",
        default=None,
        metavar="MODEL"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode for continuous prompt enhancement"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="%(prog)s 1.0.0"
    )

    args = parser.parse_args()

    # Initialize enhancer
    enhancer = PromptEnhancer(api_key=args.api_key, model=args.model)

    if args.interactive:
        print("🎬 WAN 2.2 Prompt Enhancer - Interactive Mode")
        print("Transform basic prompts into professional cinematic video generation prompts.")
        print(f"🤖 Using model: {enhancer.model}")
        print("💡 Tips: Be descriptive but concise. Examples: 'cat playing piano', 'storm over ocean'")
        print("🚪 Type 'quit', 'exit', or press Ctrl+C to stop.\n")
        
        prompt_count = 0
        while True:
            try:
                user_input = input("📝 Enter your basic prompt: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q', 'stop']:
                    print(f"\n👋 Thanks for using WAN 2.2 Prompt Enhancer! Enhanced {prompt_count} prompts.")
                    break
                    
                if not user_input:
                    print("⚠️  Please enter a prompt to enhance.\n")
                    continue
                
                print(f"\n🎯 Enhancing: '{user_input}'")
                print("✨ Generating cinematic variations...")
                print("=" * 60)
                
                enhanced = enhancer.enhance_prompt(user_input)
                print(enhanced)
                print("=" * 60)
                
                prompt_count += 1
                print(f"✅ Enhanced prompt #{prompt_count}. Ready for your next prompt!\n")
                
            except KeyboardInterrupt:
                print(f"\n\n👋 Thanks for using WAN 2.2 Prompt Enhancer! Enhanced {prompt_count} prompts.")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                print("Please try again or restart the application.\n")
    
    elif args.prompt:
        print(f"🎯 Enhancing: '{args.prompt}'")
        print("✨ Generating cinematic variations...")
        print("=" * 60)
        
        enhanced = enhancer.enhance_prompt(args.prompt)
        print(enhanced)
        print("=" * 60)
        print("✅ Enhancement complete! Use these prompts in your video generation tool.")
        
    else:
        print("🎬 WAN 2.2 Prompt Enhancer")
        print("Transform basic prompts into professional cinematic video generation prompts.\n")
        parser.print_help()
        print("\n⚠️  Please provide a prompt or use --interactive mode")
        print("💡 Quick start: python wan_prompt_enhancer.py 'your prompt here'")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("Please check your setup and try again.")
        sys.exit(1)
