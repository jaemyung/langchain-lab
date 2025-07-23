"""
02 - Prompt Templates and Engineering

This lesson covers the art and science of prompt engineering:
- Creating reusable prompt templates
- Variable substitution and formatting
- Few-shot prompting techniques
- Chat prompt templates
- Advanced prompt strategies

Run this script: python src/basics/02_prompt_templates.py
"""

import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import get_llm, print_config_status
from langchain.prompts import PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate

def basic_prompt_template():
    """
    Demonstrate basic prompt templates with variable substitution.
    
    Prompt templates allow you to create reusable prompts with
    placeholders that get filled in at runtime.
    """
    print("📝 Example 1: Basic Prompt Templates")
    print("-" * 40)
    
    try:
        llm = get_llm("auto", temperature=0.3)
        
        # Create a simple template
        template = """
        You are an expert {role} with {years} years of experience.
        
        Please explain {topic} to a {audience} in a way that is:
        - Easy to understand
        - Practical and actionable
        - Engaging and interesting
        
        Topic: {topic}
        Audience: {audience}
        """
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["role", "years", "topic", "audience"]
        )
        
        # Format the prompt with specific values
        formatted_prompt = prompt.format(
            role="Python developer",
            years="10",
            topic="object-oriented programming",
            audience="beginners"
        )
        
        print("📋 Formatted Prompt:")
        print(formatted_prompt)
        
        # Send to LLM
        response = llm.invoke(formatted_prompt)
        print(f"\n🤖 Response:\n{response.content[:300]}...")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def chat_prompt_template():
    """
    Demonstrate chat-style prompt templates.
    
    Chat templates allow you to structure conversations with
    system messages, human messages, and AI responses.
    """
    print("\n💬 Example 2: Chat Prompt Templates")
    print("-" * 40)
    
    try:
        llm = get_llm("auto", temperature=0.5)
        
        # Create a chat prompt template
        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that explains {subject} concepts clearly and concisely."),
            ("human", "Hello! I'm new to {subject}."),
            ("ai", "Hello! I'd be happy to help you learn {subject}. What specific topic would you like to start with?"),
            ("human", "{user_question}")
        ])
        
        # Format the chat prompt
        formatted_chat = chat_prompt.format_messages(
            subject="machine learning",
            user_question="What's the difference between supervised and unsupervised learning?"
        )
        
        print("📋 Chat Messages:")
        for message in formatted_chat:
            print(f"{message.type}: {message.content}")
        
        # Send to LLM
        response = llm.invoke(formatted_chat)
        print(f"\n🤖 Response:\n{response.content}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def few_shot_prompting():
    """
    Demonstrate few-shot prompting techniques.
    
    Few-shot prompting provides examples to guide the LLM's
    response format and style.
    """
    print("\n🎯 Example 3: Few-Shot Prompting")
    print("-" * 40)
    
    try:
        llm = get_llm("auto", temperature=0.2)
        
        # Define examples for few-shot learning
        examples = [
            {
                "input": "Python",
                "output": "🐍 Python: A versatile, high-level programming language known for its simplicity and readability. Great for beginners!"
            },
            {
                "input": "JavaScript", 
                "output": "⚡ JavaScript: The language of the web! Runs in browsers and servers, perfect for interactive websites and web apps."
            },
            {
                "input": "Rust",
                "output": "🦀 Rust: A systems programming language focused on safety and performance. Memory-safe without garbage collection!"
            }
        ]
        
        # Create example template
        example_template = PromptTemplate(
            input_variables=["input", "output"],
            template="Programming Language: {input}\nDescription: {output}"
        )
        
        # Create few-shot prompt
        few_shot_prompt = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_template,
            prefix="Generate engaging descriptions for programming languages in this format:",
            suffix="Programming Language: {input}\nDescription:",
            input_variables=["input"]
        )
        
        # Test with new language
        test_language = "Go"
        formatted_prompt = few_shot_prompt.format(input=test_language)
        
        print("📋 Few-Shot Prompt:")
        print(formatted_prompt)
        
        response = llm.invoke(formatted_prompt)
        print(f"\n🤖 Response:\n{response.content}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def conditional_prompting():
    """
    Demonstrate conditional prompting based on context.
    
    Sometimes you need different prompts based on the input
    or context of the conversation.
    """
    print("\n🔀 Example 4: Conditional Prompting")
    print("-" * 40)
    
    try:
        llm = get_llm("auto", temperature=0.4)
        
        def create_prompt_for_difficulty(topic, difficulty_level):
            """Create different prompts based on difficulty level."""
            
            if difficulty_level == "beginner":
                template = """
                Explain {topic} to someone who is completely new to the subject.
                Use simple language, avoid jargon, and include analogies.
                Keep it short and encouraging.
                """
            elif difficulty_level == "intermediate":
                template = """
                Explain {topic} for someone with basic knowledge.
                Include technical details but keep explanations clear.
                Provide practical examples and use cases.
                """
            else:  # advanced
                template = """
                Provide an in-depth explanation of {topic} for experts.
                Include technical specifications, edge cases, and best practices.
                Assume deep knowledge of related concepts.
                """
            
            return PromptTemplate(template=template, input_variables=["topic"])
        
        topic = "neural networks"
        difficulties = ["beginner", "intermediate", "advanced"]
        
        for difficulty in difficulties:
            print(f"\n📚 {difficulty.upper()} Level:")
            prompt = create_prompt_for_difficulty(topic, difficulty)
            formatted_prompt = prompt.format(topic=topic)
            
            response = llm.invoke(formatted_prompt)
            print(response.content[:200] + "...")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def dynamic_prompt_building():
    """
    Demonstrate building prompts dynamically based on user input.
    
    This shows how to create adaptive prompts that change based
    on the specific requirements or context.
    """
    print("\n🏗️ Example 5: Dynamic Prompt Building")
    print("-" * 40)
    
    try:
        llm = get_llm("auto", temperature=0.6)
        
        def build_writing_prompt(writing_type, audience, tone, length):
            """Build a writing prompt based on parameters."""
            
            base_template = "Write a {writing_type} for {audience} with a {tone} tone."
            
            # Add length specification
            length_specs = {
                "short": "Keep it under 100 words.",
                "medium": "Aim for 200-300 words.", 
                "long": "Write 500+ words with detailed explanations."
            }
            
            # Add tone guidance
            tone_guidance = {
                "professional": "Use formal language and industry terminology.",
                "casual": "Use conversational language and relatable examples.",
                "humorous": "Include appropriate humor and wit.",
                "educational": "Focus on teaching and clear explanations."
            }
            
            full_template = f"{base_template} {length_specs.get(length, '')} {tone_guidance.get(tone, '')}"
            
            return PromptTemplate(
                template=full_template + "\n\nTopic: {topic}",
                input_variables=["writing_type", "audience", "tone", "topic"]
            )
        
        # Test different combinations
        scenarios = [
            {
                "writing_type": "blog post",
                "audience": "tech professionals", 
                "tone": "professional",
                "length": "medium",
                "topic": "API security best practices"
            },
            {
                "writing_type": "tutorial",
                "audience": "beginners",
                "tone": "casual", 
                "length": "short",
                "topic": "Git basics"
            }
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n📝 Scenario {i}:")
            prompt = build_writing_prompt(
                scenario["writing_type"],
                scenario["audience"], 
                scenario["tone"],
                scenario["length"]
            )
            
            formatted_prompt = prompt.format(**scenario)
            print(f"Prompt: {formatted_prompt}")
            
            response = llm.invoke(formatted_prompt)
            print(f"Response: {response.content[:150]}...")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all prompt template examples."""
    print("🔬 LangChain Lab - Lesson 2: Prompt Templates")
    print("=" * 50)
    
    # Show configuration status
    print_config_status()
    
    # Run all examples
    basic_prompt_template()
    chat_prompt_template()
    few_shot_prompting()
    conditional_prompting()
    dynamic_prompt_building()
    
    print("\n🎉 Lesson 2 Complete!")
    print("💡 Key Takeaways:")
    print("   • Prompt templates make prompts reusable and maintainable")
    print("   • Variable substitution allows dynamic content")
    print("   • Few-shot examples guide LLM response format")
    print("   • Chat templates structure conversations")
    print("   • Conditional prompts adapt to different contexts")
    print("\n📚 Next: Run 'python src/basics/03_chains.py' to learn about chaining operations")

if __name__ == "__main__":
    main()
