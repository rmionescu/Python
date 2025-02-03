from baseItem import BaseItem
from baseActor import BaseActor
from itemType import ItemType


class Weapon(BaseItem):
    def __init__(self, name: str, damage: int):
        super().__init__(name, ItemType.WEAPON)
        self.damage = damage

    def use(self, target: "BaseActor"):
        if self.equipped_by is None:
            raise ValueError(f"{self.name} is not equipped. Cannot attack.")

        target.receive_damage(self.damage)
        return self.damage

    def __str__(self):
        is_equipped_by = self.equipped_by.name if self.equipped_by else 'No one'

        return (f"{self.__class__.__name__}(name='{self.name}', item_type='{self.item_type.description}', "
                f"damage={self.damage}, equipped_by='{is_equipped_by}')")
