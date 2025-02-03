# ABSTRACT CLASS
# A class that cannot be instantiated on its own; Meant to be subclassed
# They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
# 1. Prevent instantiation of the class itself
# 2. Requires children to inherited abstract methods

from abc import ABC, abstractmethod
from actorType import ActorType
from typing import Dict, TYPE_CHECKING

# Prevents circular import during runtime
if TYPE_CHECKING:
    from baseItem import BaseItem


class BaseActor(ABC):
    def __init__(self, name: str, actor_type: ActorType):
        self._name = name
        self._actor_type = actor_type

        # Default values
        self._current_health = 0
        self._max_health = 0
        self._level = 1
        self._equipped_items: Dict[str, "BaseItem"] = {}  # store the equipped items

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def actor_type(self):
        return self._actor_type

    @actor_type.setter
    def actor_type(self, value: ActorType):
        self._actor_type = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        self._level = value

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, value: int):
        value = max(value, 0)
        self._current_health = min(value, self._max_health)

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, value: int):
        self._max_health = max(value, 0)  # health cannot be negative

        # Check if health it's greater than max health and adjust
        if self._current_health > self._max_health:
            self.current_health = self._max_health

    @property
    def equipped_items(self):
        """Returns a dictionary of equipped items"""
        return self._equipped_items

    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def receive_damage(self, amount: int):
        # Each Actor should implement its own receive_damage method
        pass

    def equip(self, item: "BaseItem"):
        """
        Adds an item to equipped items. If an item with the same name exists, replaces it.
        """
        if item.equipped_by:
            return False
        item.equipped_by = self  # Mark the item equipped
        self._equipped_items[item.name] = item
        return True

    def unequip(self, item: "BaseItem"):
        """
        Remove the item from equipped items and mark it
        """
        if item.equipped_by == self:
            item.equipped_by = None
            self._equipped_items.pop(item.name)
            return True

        return False

    def get_item_by_name(self, item_name: str):
        """
        Searches for an equipped item by name.
        Returns the item if found, otherwise returns None.
        """
        return self._equipped_items.get(item_name, None)

    def __str__(self):
        equipped = ", ".join(self._equipped_items.keys()) if self.equipped_items else ""

        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"creature_type='{self.actor_type.value}', "
                f"health={self.current_health}/{self.max_health}, "
                f"equipped_items=[{equipped}])")
