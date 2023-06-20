from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    fish = Ingredient("salmão")
    fish2 = Ingredient("salmão")
    assert hash(fish) == hash('carne')
    assert fish == fish2
