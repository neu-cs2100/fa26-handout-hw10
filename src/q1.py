"""HW10 Question 1: Determining when to use inheritance versus composition

We're building a text adventure game.
Your task is to implement five classes: Item, Weapon, Inventory, Character, and Player.
You will need to decide which class relationships should use inheritance and which should use 
composition.

Item's constructor should take a `name` and a `weight` (float) as arguments and save them as 
attributes with the same names. Item's `__str__()` method should return a string in the format 
"Item(name, weight)".

Weapon's constructor should take a `name`, `weight` (float), and `damage` (int) as arguments 
and save them as attributes with the same names. A weapon is something a player can carry.
Weapon's `__str__()` method should return a string in the format "Weapon(name, weight, damage)".

Inventory's constructor should take a `capacity` (float) as an argument and save it as an 
attribute with the same name. It should also initialize an empty list to hold items.
Inventory should have the following methods:
- add(item: Item) -> bool: adds the item and returns True, unless doing so would push the 
total weight over capacity. In that case, return False and don't add it.
- remove(name: str) -> Optional[Item]: removes and returns the first item with that name, or None
if there is no item with that name.
- total_weight() -> float: returns the total weight of all items in the inventory.
- names() -> list[str]: returns a list of the names of all items in the inventory.
Inventory's `__str__()` method should return a string in the format 
"Inventory(capacity, total_weight)".

Character's constructor should take a `name` and `health` (int) as arguments and save them as 
attributes with the same names.
Character should have the following methods:
- take_damage(amount: int) -> None: reduces health, never below 0.
- is_alive() -> bool: True while health is above 0.
Character's `__str__()` method should return a string in the format "Character(name, health)".

Player's constructor should take a `name`, `health` (int), and `carry_capacity` (float) as 
arguments and save them as attributes with the same names. A player is a character in the game 
world. They can carry things and wield one weapon, so the constructor should also initialize an 
empty inventory and set the current equipped weapon to None. The current equipped weapon does not
count towards the player's carrying capacity (which is entirely dedicated to the inventory).
Player should have the following methods:
- pick_up(item: Item) -> bool: succeeds or fails at adding it to the inventory based on the 
player's inventory's carrying capacity.
- equip(weapon_name: str) -> bool: if the player is carrying a Weapon with that name, take it out 
of their inventory, wield it, and return True. Otherwise, do nothing and return False. If the 
player is already wielding a weapon, it should be returned to the inventory before equipping the 
new one. If returning the old weapon to the inventory fails due to capacity limits, do not equip 
the new weapon, keep the old weapon equipped, and return False.
- attack(target: Character) -> int: deals damage to the target and returns the amount dealt. 
The damage amount is the equipped weapon's damage, or 1 if there is no current equipped weapon.
Player's `__str__()` method should return a string in the format 
"Player(name, health, carry_capacity)".

Make sure to write tests in the tests directory. The autograder will also additionally check your 
inheritance and composition relationships, but you don't need to test those relationships.
"""
