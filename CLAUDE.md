# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys: OPENAI_API_KEY, ANTHROPIC_API_KEY
```

### Running Scripts
```bash
# Test basic setup
python src/basics/01_simple_llm.py

# Run specific learning modules
python src/basics/02_prompt_templates.py
python src/langgraph/01_simple_graph.py

# Start Jupyter for interactive notebooks
jupyter notebook notebooks/
jupyter lab notebooks/
```

### Testing and Code Quality
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_config.py -v

# Code formatting and linting
black src/
flake8 src/
```

## Project Architecture

### Core Configuration System
- **`src/config/settings.py`**: Centralized configuration management with `Settings` class
- Environment variables loaded via `python-dotenv`
- Unified LLM interface through `get_llm()` function supporting OpenAI and Anthropic providers
- Built-in API key validation and connection testing

### Learning Path Structure
The codebase follows a progressive learning structure:

1. **Basics** (`src/basics/`): Core LangChain concepts starting with simple LLM calls
2. **LangGraph** (`src/langgraph/`): Agent orchestration and state management 
3. **Advanced** (`src/advanced/`): RAG systems and custom tools
4. **Projects** (`src/projects/`): Complete application implementations

### Key Patterns
- All scripts include `sys.path.append()` to import from `config.settings`
- LLM instances created via `get_llm(provider, **kwargs)` for consistency
- Error handling with user-friendly messages and setup guidance
- Temperature and model parameters configurable per use case
- Support for both OpenAI and Anthropic providers with auto-selection

### Dependencies
- **Core**: `langchain`, `langchain-openai`, `langchain-anthropic`, `langgraph`
- **Development**: `pytest`, `black`, `flake8` for testing and code quality
- **Optional**: `streamlit`, `jupyter`, `chromadb`, `faiss-cpu` for advanced features

### Environment Variables
Required:
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` (at least one)

Optional:
- `LANGCHAIN_TRACING_V2`: Enable LangSmith tracing
- `LANGCHAIN_API_KEY`: LangSmith API key  
- `LANGCHAIN_PROJECT`: Project name for tracing
- `DEBUG`: Enable debug mode
- `LOG_LEVEL`: Logging verbosity