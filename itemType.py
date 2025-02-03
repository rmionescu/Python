from enum import Enum


class ItemType(Enum):
    WEAPON = ("Weapon", True, False, False)
    CONSUMABLE = ("Consumable", False, True, False)
    EQUIPMENT = ("Equipment", False, False, True)

    def __init__(self, description: str, can_attack: bool, can_consume: bool, can_equip: bool):
        self.description = description
        self.can_attack = can_attack
        self.is_consumable = can_consume
        self.can_equip = can_equip
