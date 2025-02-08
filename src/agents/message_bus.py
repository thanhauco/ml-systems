from typing import List, Callable, Dict, Any
import collections

class Message:
    def __init__(self, sender: str, channel: str, content: Any):
        self.sender = sender
        self.channel = channel
        self.content = content

class AgentBus:
    """
    Pub/Sub system for inter-agent communication.
    """
    def __init__(self):
        self._subscribers = collections.defaultdict(list)
        self._history = []

    def subscribe(self, channel: str, callback: Callable[[Message], None]):
        self._subscribers[channel].append(callback)

    def publish(self, sender: str, channel: str, content: Any):
        msg = Message(sender, channel, content)
        self._history.append(msg)
        print(f"[BUS] {sender} -> {channel}: {str(content)[:50]}...")
        
        for callback in self._subscribers[channel]:
            try:
                callback(msg)
            except Exception as e:
                print(f"Error in subscriber: {e}")

    def get_history(self) -> List[Message]:
        return self._history
