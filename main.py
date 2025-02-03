from player import Player
from beast import Beast
from weapon import Weapon
from actorType import ActorType


def equip_item(actor, item) -> None:
    equipped_successfully = actor.equip(item)
    if equipped_successfully:
        print(f"{actor.name} has equipped {item.name}.")
    else:
        print(f"{actor.name} failed to equip {item.name}.")


def main() -> None:
    # Create Actors
    fighter = Player(name="Aran", actor_type=ActorType.PC, actor_class="fighter")
    wolf = Beast(name="Wolf", actor_type=ActorType.MONSTER, max_health=20)

    # Display initial stats
    print("----- Initial Stats -----")
    print(f"Player: {fighter}")
    print(f"Beast: {wolf}\n")

    # Create a Weapon
    dagger = Weapon(name="Dagger", damage=4)
    steel_sword = Weapon(name="Steel Sword", damage=8)
    wolf_claw = Weapon(name="Wolf Claw", damage=6)
    print(steel_sword)
    print(wolf_claw)

    # Equip weapons
    equip_item(fighter, steel_sword)
    equip_item(wolf, wolf_claw)
    print("\n")

    # Attacks
    print("----- Attacking with a non equipped item it's not possible -----")
    # dagger.use(wolf)
    print("\n")

    print("----- First Attack -----")
    print(f"Before Attack - Beast: {wolf}")
    damage_dealt = steel_sword.use(wolf)
    print(f"{fighter.name} attacked {wolf.name} for {damage_dealt} damage!")
    print(f"After Attack - Beast: {wolf}\n")

    # Level up the Player
    new_level = fighter.level_up()
    print(f"----- Level Up -----")
    print(f"{fighter.name} leveled up to level {new_level}!")
    print(f"New Stats - Player: {fighter}\n")

    # Unequip the weapon
    fighter.unequip(steel_sword)
    print("----- After Unequipping Weapon -----")
    print(f"Player: {fighter}")
    print(f"Weapon {steel_sword.name} equipped_by: {steel_sword.equipped_by}")


if __name__ == "__main__":
    main()
