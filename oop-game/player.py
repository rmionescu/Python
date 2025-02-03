from actorType import ActorType
from baseActor import BaseActor
from random import randint

hit_die_values = {
    "fighter": 12,
    "wizard": 6,
    "ranger": 8,
}


class Player(BaseActor):
    def __init__(self, name: str, actor_type: ActorType, actor_class: str):
        if actor_class not in hit_die_values:
            raise ValueError(f"Invalid class '{actor_class}'. Allowed classes: {', '.join(hit_die_values.keys())}")
        super().__init__(name, actor_type)
        self._max_health = hit_die_values[actor_class]
        self._current_health = self._max_health
        self._actor_class = actor_class

    @staticmethod
    def is_class_valid(class_name: str):
        return class_name in hit_die_values

    def level_up(self):
        """
        When a Player level up the max HP increases
        """
        self.level += 1
        base_die = hit_die_values[self._actor_class]
        self._max_health += randint(1, base_die)
        return self.level

    def receive_damage(self, amount: int):
        # Player damage will be the amount for now
        self.current_health = self._current_health - amount
        return self
