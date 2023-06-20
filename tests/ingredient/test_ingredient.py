from src.models.ingredient import (
    Ingredient,
    Restriction,
  )  # noqa: F401, E261, E501


def test_ingredient():
    fish = Ingredient("salmão")
    fish2 = Ingredient("salmão")
    meat = Ingredient("carne")
    assert hash(fish) == hash(fish2)
    assert fish == fish2
    assert hash(fish) != hash(meat)
    assert repr(fish) == "Ingredient('salmão')"
    assert fish.name == 'salmão'
    assert fish.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_MEAT,
    }
    print(fish.restrictions)
