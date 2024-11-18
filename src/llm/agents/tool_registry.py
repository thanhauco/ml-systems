from typing import Callable, Dict

class ToolRegistry:
    """
    Decorator-based registry for Agent tools.
    """
    
    def __init__(self):
        self.tools: Dict[str, Callable] = {}
        self.descriptions: Dict[str, str] = {}

    def register(self, description: str):
        def decorator(func):
            self.tools[func.__name__] = func
            self.descriptions[func.__name__] = description
            return func
        return decorator

    def get_tool_prompt(self):
        prompt = "Available Tools:\n"
        for name, desc in self.descriptions.items():
            prompt += f"- {name}: {desc}\n"
        return prompt

registry = ToolRegistry()

@registry.register("Get current weather for a city. Args: city")
def get_weather(city: str):
    return f"Weather in {city} is Sunny."
