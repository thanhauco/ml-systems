from collections import deque

class ConversationMemory:
    """
    Manages chat history buffer.
    """
    
    def __init__(self, max_turns=10):
        self.buffer = deque(maxlen=max_turns)

    def add_user_message(self, msg: str):
        self.buffer.append({"role": "user", "content": msg})

    def add_ai_message(self, msg: str):
        self.buffer.append({"role": "assistant", "content": msg})

    def get_prompt_text(self):
        text = ""
        for msg in self.buffer:
            text += f"{msg['role'].title()}: {msg['content']}\n"
        return text
