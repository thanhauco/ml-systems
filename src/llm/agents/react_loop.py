class ReActAgent:
    """
    Implements Reason+Act loop.
    """
    
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def run(self, goal: str):
        history = f"Goal: {goal}\n"
        
        for i in range(5): # Max steps
            print(f"Step {i+1}...")
            # 1. Thought
            # thought = llm(history + "Thought:")
            thought = "I need to check the weather."
            
            # 2. Action
            # action = llm(history + "Action:")
            action = "get_weather('London')"
            
            print(f"Thought: {thought}")
            print(f"Action: {action}")
            
            # 3. Observation
            # obs = tools.execute(action)
            obs = "Sunny, 20C"
            print(f"Obs: {obs}")
            
            history += f"Thought: {thought}\nAction: {action}\nObservation: {obs}\n"
            
            if "Final Answer" in action:
                return action
                
        return "Max steps reached."


