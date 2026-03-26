import os
import json
from .recipe import Recipe

class RecipeService:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.data_path = os.path.join(BASE_DIR, "data", "recipes.json")

        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)

        if not os.path.exists(self.data_path):
            with open(self.data_path, "w") as f:
                json.dump([], f)

    def load_recipes(self):
        with open(self.data_path, "r") as f:
            return json.load(f)

    def save_all(self, recipes):
        with open(self.data_path, "w") as f:
            json.dump(recipes, f, indent=4)

    def add_recipe(self, recipe: Recipe):
        recipes = self.load_recipes()
        recipes.append(recipe.to_dict())
        self.save_all(recipes)

    def delete_recipe(self, index):
        recipes = self.load_recipes()
        if 0 <= index < len(recipes):
            recipes.pop(index)
            self.save_all(recipes)

    def update_recipe(self, index, recipe: Recipe):
        recipes = self.load_recipes()
        if 0 <= index < len(recipes):
            recipes[index] = recipe.to_dict()
            self.save_all(recipes)
            
