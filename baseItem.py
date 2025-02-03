# ABSTRACT CLASS
# A class that cannot be instantiated on its own; Meant to be subclassed
# They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
# 1. Prevent instantiation of the class itself
# 2. Requires children to inherited abstract methods

from abc import ABC, abstractmethod
from itemType import ItemType
from typing import TYPE_CHECKING

# Prevents circular imports when not type checking
if TYPE_CHECKING:
    from baseActor import BaseActor


class BaseItem(ABC):
    def __init__(self, name: str, item_type: ItemType):
        self.name = name
        self.item_type = item_type
        self._equipped_by = None  # BaseActor that owns the item

    @property
    def equipped_by(self):
        return self._equipped_by

    @equipped_by.setter
    def equipped_by(self, target: "BaseActor"):
        """Sets the owner of the item"""
        self._equipped_by = target

    @abstractmethod
    def use(self, target: "BaseActor"):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(name='{self.name}', item_type='{self.item_type.description}'"
