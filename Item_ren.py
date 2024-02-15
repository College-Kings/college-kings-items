from dataclasses import dataclass
from typing import Optional

"""renpy
init python:
"""


@dataclass(frozen=True)
class Item:
    name: str
    cost: int = -1
    idle_image: Optional[str] = None
    hover_image: Optional[str] = None
    insensitive_image: Optional[str] = None

    def __hash__(self) -> int:
        return hash(self.name)
