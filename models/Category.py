from __future__ import annotations

import uuid
from typing import Optional
from models.Attribute import Attribute
from models.Item import Item


class Category:
    def __init__(self, name: str, category_id: Optional[uuid.UUID] = None, parent: Optional[Category] = None):
        self.id = category_id if category_id else uuid.uuid1()
        self.name = name
        self.parent: Optional[Category] = parent
        self.attributes: list[Attribute] = []
        self.children: list[Category] = []
        self.items: list[Item] = []

    def add_child(self, other: Category) -> None:
        self.children.append(other)
        map(lambda attribute: other.attributes.append(attribute), self.attributes)

    def add_attribute(self, attribute: Attribute) -> None:
        self.attributes.append(attribute)
        map(lambda category: category.add_attribute(attribute), self.children)

    def __iter__(self):
        return list.__iter__(self.children)

