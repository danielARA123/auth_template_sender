from dataclasses import dataclass

@dataclass
class DefaultHeaders:
    authorization: str
    content_type: str = "application/json"

    def to_dict(self) -> dict:
        return {
            'Authorization': self.authorization,
            'Content-Type': self.content_type,
        }