from dataclasses import dataclass
from enum import Enum

class Role(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"


@dataclass
class Message:
    role: Role
    content: str
    
    # transform the message to a dictionary
    def to_dict(self):
        return {
            "role": self.role.value,
            "content": self.content,
        }