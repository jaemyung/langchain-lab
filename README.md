# LangChain Lab 🔬

A comprehensive learning environment for experimenting with LangChain and LangGraph frameworks in Python.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- OpenAI API key and/or Anthropic API key

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/langchain-lab.git
cd langchain-lab

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your API keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### Test Your Setup
```bash
# Run basic LangChain test
python src/basics/01_simple_llm.py

# Run LangGraph test
python src/langgraph/01_simple_graph.py
```

## 📁 Project Structure

```
langchain-lab/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── src/                       # Source code
│   ├── __init__.py
│   ├── config/                # Configuration utilities
│   │   ├── __init__.py
│   │   └── settings.py        # API keys and settings management
│   ├── basics/                # LangChain fundamentals
│   │   ├── __init__.py
│   │   ├── 01_simple_llm.py
│   │   ├── 02_prompt_templates.py
│   │   ├── 03_chains.py
│   │   └── 04_memory_agents.py
│   ├── langgraph/             # LangGraph experiments
│   │   ├── __init__.py
│   │   ├── 01_simple_graph.py
│   │   ├── 02_conditional_routing.py
│   │   └── 03_multi_agent.py
│   ├── advanced/              # Advanced topics
│   │   ├── __init__.py
│   │   ├── rag_system.py
│   │   └── custom_tools.py
│   └── projects/              # Complete projects
│       ├── __init__.py
│       └── chatbot_system.py
├── notebooks/                 # Jupyter notebooks
│   ├── 01_langchain_tutorial.ipynb
│   └── 02_langgraph_experiments.ipynb
├── tests/                     # Unit tests
│   ├── __init__.py
│   └── test_config.py
└── docs/                      # Documentation
    └── learning_guide.md
```

## 🎯 Learning Path

### Phase 1: LangChain Basics (40 minutes)
1. **Simple LLM Usage** (`src/basics/01_simple_llm.py`)
   - Basic API calls
   - Error handling
   - Multiple providers

2. **Prompt Engineering** (`src/basics/02_prompt_templates.py`)
   - Template creation
   - Variable injection
   - Few-shot prompting

3. **Chains** (`src/basics/03_chains.py`)
   - Sequential chains
   - Parallel execution
   - Custom chains

### Phase 2: Memory & Agents (30 minutes)
4. **Memory Systems** (`src/basics/04_memory_agents.py`)
   - Conversation memory
   - Entity memory
   - Custom memory

### Phase 3: LangGraph (50 minutes)
5. **Simple Graphs** (`src/langgraph/01_simple_graph.py`)
   - State management
   - Node creation
   - Edge definition

6. **Conditional Logic** (`src/langgraph/02_conditional_routing.py`)
   - Decision nodes
   - Dynamic routing
   - Error handling

7. **Multi-Agent Systems** (`src/langgraph/03_multi_agent.py`)
   - Agent coordination
   - Shared state
   - Communication patterns

### Phase 4: Real Projects (20 minutes)
8. **Complete Chatbot** (`src/projects/chatbot_system.py`)
   - Full implementation
   - Production considerations

## 🧪 Running Experiments

### Individual Scripts
```bash
# Basic LangChain
python src/basics/01_simple_llm.py
python src/basics/02_prompt_templates.py

# LangGraph
python src/langgraph/01_simple_graph.py
python src/langgraph/02_conditional_routing.py
```

### Interactive Notebooks
```bash
# Start Jupyter
jupyter notebook notebooks/

# Or use Jupyter Lab
jupyter lab notebooks/
```

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_config.py -v
```

## 🔧 Configuration

The project uses environment variables for API keys and settings:

- `OPENAI_API_KEY`: Your OpenAI API key
- `ANTHROPIC_API_KEY`: Your Anthropic API key  
- `LANGCHAIN_TRACING_V2`: Enable LangSmith tracing (optional)
- `LANGCHAIN_API_KEY`: LangSmith API key (optional)
- `LANGCHAIN_PROJECT`: Project name for tracing (optional)

## 📚 Resources

### Official Documentation
- [LangChain Python Docs](https://python.langchain.com/docs/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangSmith Platform](https://docs.smith.langchain.com/)

### Learning Materials
- [LangChain Academy](https://academy.langchain.com/)
- [LangGraph Tutorials](https://langchain-ai.github.io/langgraph/tutorials/)
- [Community Examples](https://github.com/langchain-ai/langchain/tree/master/cookbook)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the amazing framework
- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration
- The open-source AI community for inspiration and examples

---

**Happy Learning!** 🎉

For questions or issues, please open a GitHub issue or reach out to the community.
