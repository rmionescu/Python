import pytest
from unittest.mock import patch

from player import Player
from beast import Beast
from weapon import Weapon
from actorType import ActorType


@pytest.fixture
def fighter():
    """Return a Fighter-class Player."""
    return Player(name="Aran", actor_type=ActorType.PC, actor_class="fighter")


@pytest.fixture
def wolf():
    """Return a Beast with 20 HP."""
    return Beast(name="Wolf", actor_type=ActorType.MONSTER, max_health=20)


@pytest.fixture
def sword():
    """Return a Weapon with 6 damage."""
    return Weapon(name="Steel Sword", damage=6)


def test_player_initialization(fighter):
    """
    Test that the Player is initialized correctly.
    - Ensures that max_health and current_health match the Fighter's hit die (12).
    - Checks default level is 1.
    """
    assert fighter.name == "Aran"
    assert fighter.actor_type == ActorType.PC
    assert fighter.level == 1
    assert fighter.max_health == 12
    assert fighter.current_health == 12


def test_beast_initialization(wolf):
    """
    Test that the Beast is initialized correctly.
    """
    assert wolf.name == "Wolf"
    assert wolf.actor_type == ActorType.MONSTER
    assert wolf.max_health == 20
    assert wolf.current_health == 20


def test_weapon_initialization(sword):
    """
    Test that the Weapon is initialized correctly.
    """
    assert sword.name == "Steel Sword"
    assert sword.damage == 6
    # Check the item_type is correct
    from itemType import ItemType
    assert sword.item_type == ItemType.WEAPON
    assert sword.equipped_by is None


def test_player_level_up(fighter):
    """
    Test level up without mocking. Because there's a random roll,
    we only check that the level increments by 1.
    """
    old_level = fighter.level
    fighter.level_up()
    assert fighter.level == old_level + 1
    # current_health can vary. We won't check it precisely here.


@patch("player.randint", return_value=5)
def test_player_level_up_random(mock_rand, fighter):
    """
    Test Player level up with mocked random.randint.
    This ensures max_health increases by 5 for a Fighter.
    """
    old_level = fighter.level
    old_hp = fighter.max_health

    new_level = fighter.level_up()

    # Check that our mock was called with (1, 12) for the Fighter class
    mock_rand.assert_called_once_with(1, 12)
    assert new_level == old_level + 1
    assert fighter.max_health == old_hp + 5


def test_player_receive_damage(fighter):
    """
    Test that a Player's current_health is reduced correctly.
    """
    old_hp = fighter.current_health
    dmg = 5
    fighter.receive_damage(dmg)
    assert fighter.current_health == old_hp - dmg
    # Also ensure it doesn't go below 0 if damage is huge
    fighter.receive_damage(9999)
    assert fighter.current_health == 0


def test_beast_receive_damage(wolf):
    """
    By default, Beast has a toughness of 2: it subtracts 2 from incoming damage.
    So receiving 5 damage effectively reduces HP by 3.
    """
    old_hp = wolf.current_health
    wolf.receive_damage(5)
    # expect 5 - 2 = 3 net damage
    assert wolf.current_health == old_hp - 3


def test_equip_unequip(fighter, sword):
    """
    Test equipping and unequipping an item on a Player.
    """
    assert sword.equipped_by is None

    # Equip the sword
    equipped_success = fighter.equip(sword)
    assert equipped_success is True
    assert sword.equipped_by == fighter
    assert fighter.get_item_by_name("Steel Sword") is sword

    # Unequip the sword
    unequipped_success = fighter.unequip(sword)
    assert unequipped_success is True
    assert sword.equipped_by is None
    assert fighter.get_item_by_name("Steel Sword") is None


@patch.object(Beast, "receive_damage")
def test_weapon_use(mock_receive_damage, fighter, wolf, sword):
    """
    Test that using a weapon calls the target's receive_damage method
    with the correct damage.
    We mock Beast.receive_damage to verify the call without actually
    changing the Beast's health in this test.
    """
    # Equip the sword to the fighter
    fighter.equip(sword)

    # Attack the wolf
    damage_dealt = sword.use(wolf)

    # The method .receive_damage should be called once with '6'
    mock_receive_damage.assert_called_once_with(6)
    assert damage_dealt == 6


def test_weapon_use_not_equipped(sword, wolf):
    """
    Attempting to use a weapon that is not equipped
    should raise a ValueError.
    """
    with pytest.raises(ValueError) as exc_info:
        sword.use(wolf)
    assert "is not equipped" in str(exc_info.value)
