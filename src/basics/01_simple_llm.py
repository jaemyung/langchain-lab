"""
01 - Simple LLM Usage Examples

This is your first step into LangChain! This script demonstrates:
- How to make basic LLM calls
- Error handling for API issues
- Comparing different LLM providers
- Understanding response formats

Run this script: python src/basics/01_simple_llm.py
"""

import sys
import os

# Add the src directory to Python path so we can import our config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import get_llm, print_config_status, test_llm_connection

def simple_llm_call():
    """
    Demonstrate the most basic LLM usage.
    
    This is the foundation of all LangChain applications - making a simple
    call to an LLM and getting a response.
    """
    print("🚀 Example 1: Simple LLM Call")
    print("-" * 40)
    
    try:
        # Get an LLM instance (auto-selects based on available API keys)
        llm = get_llm("auto", temperature=0.7)
        
        # Make a simple call
        response = llm.invoke("Hello! Please introduce yourself and tell me what you can help with.")
        
        print(f"Response: {response.content}")
        print(f"Response Type: {type(response)}")
        print(f"Has additional info: {hasattr(response, 'response_metadata')}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have set up your .env file with API keys")

def compare_providers():
    """
    Compare responses from different LLM providers.
    
    This shows how LangChain provides a unified interface across
    different LLM providers.
    """
    print("\n🔄 Example 2: Comparing LLM Providers")
    print("-" * 40)
    
    question = "What are the key benefits of using LangChain for AI development?"
    
    providers = ["openai", "anthropic"]
    
    for provider in providers:
        try:
            print(f"\n🤖 {provider.upper()} Response:")
            llm = get_llm(provider, temperature=0.3)
            response = llm.invoke(question)
            print(response.content[:200] + "..." if len(response.content) > 200 else response.content)
            
        except Exception as e:
            print(f"❌ {provider.upper()} failed: {e}")

def demonstrate_parameters():
    """
    Show how different parameters affect LLM responses.
    
    Temperature, max_tokens, and other parameters significantly
    affect the LLM's behavior.
    """
    print("\n⚙️ Example 3: LLM Parameters")
    print("-" * 40)
    
    prompt = "Write a creative story in exactly one sentence about a robot learning to paint."
    
    # Test different temperature settings
    temperatures = [0.0, 0.5, 1.0]
    
    for temp in temperatures:
        try:
            print(f"\n🌡️ Temperature {temp}:")
            llm = get_llm("auto", temperature=temp, max_tokens=100)
            response = llm.invoke(prompt)
            print(response.content)
            
        except Exception as e:
            print(f"❌ Error with temperature {temp}: {e}")

def batch_processing():
    """
    Demonstrate batch processing of multiple queries.
    
    Sometimes you need to process multiple queries efficiently.
    LangChain provides batch processing capabilities.
    """
    print("\n📦 Example 4: Batch Processing")
    print("-" * 40)
    
    questions = [
        "What is machine learning?",
        "Explain neural networks in simple terms.",
        "What are the benefits of prompt engineering?"
    ]
    
    try:
        llm = get_llm("auto", temperature=0.2)
        
        print("Processing questions individually:")
        for i, question in enumerate(questions, 1):
            response = llm.invoke(question)
            print(f"Q{i}: {question}")
            print(f"A{i}: {response.content[:100]}...\n")
            
    except Exception as e:
        print(f"❌ Batch processing error: {e}")

def streaming_response():
    """
    Demonstrate streaming responses for real-time applications.
    
    Streaming is crucial for building responsive chat applications
    where users see text appearing in real-time.
    """
    print("\n🌊 Example 5: Streaming Responses")
    print("-" * 40)
    
    try:
        llm = get_llm("auto", temperature=0.7)
        
        prompt = "Tell me an interesting fact about space exploration."
        
        print("Streaming response (watch text appear in real-time):")
        print("Response: ", end="", flush=True)
        
        # Stream the response
        for chunk in llm.stream(prompt):
            print(chunk.content, end="", flush=True)
        
        print("\n✅ Streaming complete!")
        
    except Exception as e:
        print(f"❌ Streaming error: {e}")

def main():
    """Run all examples in sequence."""
    print("🔬 LangChain Lab - Lesson 1: Simple LLM Usage")
    print("=" * 50)
    
    # Show configuration status first
    print_config_status()
    
    # Test connection
    print("🔌 Testing LLM Connection...")
    if not test_llm_connection():
        print("❌ Cannot proceed without a working LLM connection.")
        print("💡 Please check your .env file and API keys.")
        return
    
    # Run all examples
    simple_llm_call()
    compare_providers()
    demonstrate_parameters()
    batch_processing()
    streaming_response()
    
    print("\n🎉 Lesson 1 Complete!")
    print("💡 Next: Run 'python src/basics/02_prompt_templates.py' to learn about prompt engineering")

if __name__ == "__main__":
    main()
