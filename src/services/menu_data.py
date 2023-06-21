import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._load_data(source_path)

    def _load_data(self, source_path: str):
        data = pd.read_csv(source_path)
        dishes = set()

        grouped = data.groupby(['dish', 'price'])
        for (_, _), group in grouped:
            dish_name, dish_price = group[
                'dish'].iloc[0], group['price'].iloc[0]
            dish = Dish(dish_name, float(dish_price))

            for _, row in group.iterrows():
                ingredient = Ingredient(row['ingredient'])
                dish.add_ingredient_dependency(
                    ingredient, int(row['recipe_amount']))

            dishes.add(dish)

        return dishes

    def _validate_source_path(self, source_path: str):
        if not isinstance(source_path, str):
            raise TypeError("source_path must be a string")
        if not source_path.endswith(".csv"):
            raise ValueError("The file must have a .csv extension")
