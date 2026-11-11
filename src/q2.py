"""HW10 Question 2: Encapsulation

Your task is to write the following three classes:

1. GamePlayer: A base class representing a player in an online game.

   - The constructor takes two parameters: `player_id` (str) and `handle` (str). A valid handle 
     is between 4 and 12 characters long (inclusive), starts with a letter, and contains only 
     letters and numbers. A valid player ID is a non-empty string. If the player ID or handle are 
     invalid, raise a ValueError.
   - player_id should be stored in a private attribute named with two underscores (e.g., 
     `self.__player_id`). It should only be externally visible through a read-only 
     property named `player_id`
   - `handle` should be stored in a "protected" attribute named with a single underscore (e.g., 
     `self._handle`). It should only be externally accessible through a property named `handle` 
     with both a getter and a setter (which validates the handle).
   - Two `GamePlayer` instances are considered equal if they have the same player ID and handle.
   - The `__str__()` method should return the handle.

2. RegularPlayer: Inherits from GamePlayer without adding any new attributes or methods.

3. PremiumPlayer: Inherits from GamePlayer, representing a player with an active premium 
    subscription.

   - The constructor should take three parameters: `player_id` (str), `handle` (str),
     and `is_subscribed` (bool).
   - If `is_subscribed` is False, raise a ValueError in the constructor.
   - Overwrite the `handle` property so that it returns the handle with
     a star and a space prepended (for example, "★ User123").
   - The `__str__()` method should also return the handle with a star and a space prepended.
   - Reuse code whenever possible.

Make sure to write tests in the tests directory.
"""
