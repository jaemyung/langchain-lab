"""
Configuration settings and utilities for LangChain Lab.

This module handles API keys, model configuration, and provides
helper functions to get LLM instances.
"""

import os
import logging
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Configuration settings for the application."""
    
    # API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    LANGCHAIN_API_KEY: Optional[str] = os.getenv("LANGCHAIN_API_KEY")
    
    # LangSmith Configuration
    LANGCHAIN_TRACING_V2: bool = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT", "langchain-lab")
    
    # Model Defaults
    DEFAULT_OPENAI_MODEL: str = os.getenv("DEFAULT_OPENAI_MODEL", "gpt-3.5-turbo")
    DEFAULT_ANTHROPIC_MODEL: str = os.getenv("DEFAULT_ANTHROPIC_MODEL", "claude-3-sonnet-20240229")
    
    # Application Settings
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate_api_keys(cls) -> dict:
        """
        Validate that required API keys are present.
        
        Returns:
            dict: Status of each API key (present/missing)
        """
        status = {
            "openai": bool(cls.OPENAI_API_KEY),
            "anthropic": bool(cls.ANTHROPIC_API_KEY),
            "langsmith": bool(cls.LANGCHAIN_API_KEY)
        }
        
        if not cls.OPENAI_API_KEY and not cls.ANTHROPIC_API_KEY:
            raise ValueError(
                "At least one of OPENAI_API_KEY or ANTHROPIC_API_KEY must be set. "
                "Please check your .env file."
            )
        
        return status
    
    @classmethod
    def setup_logging(cls):
        """Set up logging configuration."""
        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL.upper()),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

def get_llm(provider: str = "auto", model: Optional[str] = None, **kwargs):
    """
    Get an LLM instance based on provider.
    
    Args:
        provider: LLM provider ("openai", "anthropic", or "auto")
        model: Specific model name (optional)
        **kwargs: Additional arguments passed to the LLM constructor
        
    Returns:
        LLM instance
        
    Raises:
        ValueError: If provider is not supported or API key is missing
    """
    Settings.validate_api_keys()
    
    if provider == "auto":
        # Auto-select based on available API keys
        if Settings.OPENAI_API_KEY:
            provider = "openai"
        elif Settings.ANTHROPIC_API_KEY:
            provider = "anthropic"
        else:
            raise ValueError("No API keys found. Please set OPENAI_API_KEY or ANTHROPIC_API_KEY")
    
    if provider.lower() == "openai":
        if not Settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        from langchain_openai import ChatOpenAI
        
        model = model or Settings.DEFAULT_OPENAI_MODEL
        return ChatOpenAI(
            api_key=Settings.OPENAI_API_KEY,
            model=model,
            **kwargs
        )
    
    elif provider.lower() == "anthropic":
        if not Settings.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        from langchain_anthropic import ChatAnthropic
        
        model = model or Settings.DEFAULT_ANTHROPIC_MODEL
        return ChatAnthropic(
            api_key=Settings.ANTHROPIC_API_KEY,
            model=model,
            **kwargs
        )
    
    else:
        raise ValueError(f"Unsupported provider: {provider}. Use 'openai' or 'anthropic'")

def print_config_status():
    """Print current configuration status."""
    print("🔧 Configuration Status")
    print("=" * 40)
    
    status = Settings.validate_api_keys()
    
    print(f"OpenAI API Key: {'✅ Set' if status['openai'] else '❌ Missing'}")
    print(f"Anthropic API Key: {'✅ Set' if status['anthropic'] else '❌ Missing'}")
    print(f"LangSmith API Key: {'✅ Set' if status['langsmith'] else '❌ Missing (Optional)'}")
    print(f"LangSmith Tracing: {'✅ Enabled' if Settings.LANGCHAIN_TRACING_V2 else '❌ Disabled'}")
    print(f"Project Name: {Settings.LANGCHAIN_PROJECT}")
    print(f"Debug Mode: {'✅ On' if Settings.DEBUG else '❌ Off'}")
    print(f"Log Level: {Settings.LOG_LEVEL}")
    print()
    
    if status['openai']:
        print(f"🤖 Default OpenAI Model: {Settings.DEFAULT_OPENAI_MODEL}")
    if status['anthropic']:
        print(f"🧠 Default Anthropic Model: {Settings.DEFAULT_ANTHROPIC_MODEL}")

def test_llm_connection(provider: str = "auto"):
    """
    Test LLM connection with a simple query.
    
    Args:
        provider: LLM provider to test
        
    Returns:
        bool: True if connection successful, False otherwise
    """
    try:
        llm = get_llm(provider)
        response = llm.invoke("Hello! Please respond with just 'OK' to test the connection.")
        print(f"✅ {provider.upper()} connection successful!")
        print(f"Response: {response.content}")
        return True
    except Exception as e:
        print(f"❌ {provider.upper()} connection failed: {str(e)}")
        return False

# Initialize logging when module is imported
Settings.setup_logging()
