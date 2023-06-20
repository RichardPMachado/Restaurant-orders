# import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("salmão com salada", 10)
    assert dish.name == "salmão com salada"
    assert dish.price == 'R$ 80,00'
