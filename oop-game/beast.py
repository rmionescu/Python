from baseActor import BaseActor
from actorType import ActorType


class Beast(BaseActor):
    def __init__(self, name: str, actor_type: ActorType, max_health: int):
        super().__init__(name, actor_type)
        self._max_health = max_health
        self._current_health = max_health
        self._toughness = 2  # Reduce damage taken by 2

    def level_up(self):
        """
        A beast does not level up
        """
        raise ValueError(f"{self.actor_type.value} cannot level up!")

    def receive_damage(self, amount: int):
        # Beast will take less damage because of toughness
        self.current_health = self._current_health - amount + self._toughness
        return self
