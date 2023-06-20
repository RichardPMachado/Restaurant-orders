import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("salmão com salada", 80)
    assert dish.name == "salmão com salada"
    assert dish.price == 80
    dish.add_ingredient_dependency('salmão', 2)
    print(dish.get_ingredients())
    assert dish.get_ingredients() == {'salmão'}

    with pytest.raises(
        ValueError, match='Dish price must be greater then zero.'
    ):
        Dish("doce de coco", -1)
    with pytest.raises(
        TypeError, match='Dish price must be float.'
    ):
        Dish("doce de coco", '2')
