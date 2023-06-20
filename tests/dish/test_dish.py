import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("salmão com salada", 80.00)
    assert dish.name == "salmão com salada"
    assert dish.price == 80.00
    dish.add_ingredient_dependency(Ingredient("salmão"), 2)
    assert dish.get_ingredients() == {Ingredient("salmão")}
    assert dish.__repr__() == "Dish('salmão com salada', R$80.00)"
    assert dish.__eq__(Dish('salmão com salada', 80.00)) is True
    assert dish.__hash__() == hash(Dish("salmão com salada", 80.00))
    assert dish.__hash__() != hash(Dish("salmão com salada", 70.00))
    assert dish.get_restrictions() == Ingredient("salmão").restrictions
    # print(Ingredient("salmão").restrictions)

    with pytest.raises(
        ValueError, match='Dish price must be greater then zero.'
    ):
        Dish("doce de coco", -1)

    with pytest.raises(
        TypeError, match='Dish price must be float.'
    ):
        Dish("doce de coco", '2')
