from typing import Dict, Any
from .message_bus import AgentBus, Message

class SwarmOrchestrator:
    """
    Manages the lifecycle and routing of a multi-agent swarm.
    """
    
    def __init__(self):
        self.bus = AgentBus()
        self.agents = {}
        self.active_goal = None

    def register_agent(self, name: str, agent_func):
        self.agents[name] = agent_func
        # Subscribe agent to its own channel
        self.bus.subscribe(name, self._create_handler(name, agent_func))
        print(f"Agent '{name}' registered.")

    def _create_handler(self, name: str, func):
        def handler(msg: Message):
            if msg.sender != name: # Don't reply to self
                response = func(msg.content)
                if response:
                    # By default, reply to sender or broadcast?
                    # Simple swarm: reply to 'main' or sender
                    self.bus.publish(name, "main", response)
        return handler

    def run_mission(self, goal: str, start_agent: str):
        self.active_goal = goal
        print(f"Starting Swarm Mission: {goal}")
        self.bus.publish("main", start_agent, {"instruction": goal})

# Mock agent logic
def research_agent(payload):
    return f"Research results for: {payload.get('instruction')}"

def writer_agent(payload):
    return f"Drafting content based on: {payload}"
