import customtkinter as ctk
from .base_window import BaseWindow
from .recipe_service import RecipeService
from .recipe import Recipe
from .report_generator import ReportGenerator

class RecipeApp(BaseWindow):
    def __init__(self):
        super().__init__()

        self.service = RecipeService()
        self.selected_index = None

        # Title
        ctk.CTkLabel(self, text="Recipe App", font=("Arial", 20)).pack(pady=10)

        # Inputs
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Recipe Name")
        self.name_entry.pack(pady=5)

        self.ing_entry = ctk.CTkEntry(self, placeholder_text="Ingredients")
        self.ing_entry.pack(pady=5)

        self.ins_entry = ctk.CTkEntry(self, placeholder_text="Instructions")
        self.ins_entry.pack(pady=5)

        # Buttons
        ctk.CTkButton(self, text="Add Recipe", command=self.add_recipe).pack(pady=5)
        ctk.CTkButton(self, text="Update Recipe", command=self.update_recipe).pack(pady=5)
        ctk.CTkButton(self, text="Delete Recipe", command=self.delete_recipe).pack(pady=5)
        ctk.CTkButton(self, text="Generate Report", command=self.generate_report).pack(pady=5)

        # Output box
        self.listbox = ctk.CTkTextbox(self, height=180)
        self.listbox.pack(pady=10)

        self.listbox.bind("<ButtonRelease-1>", self.select_recipe)

        self.refresh_list()

    # ---------------- VALIDATION ----------------
    def validate_input(self, name, ingredients, instructions):
        if not name.strip():
            return "Recipe name is required"
        if not ingredients.strip():
            return "Ingredients are required"
        if not instructions.strip():
            return "Instructions are required"
        return None

    # ---------------- ACTIONS ----------------

    def add_recipe(self):
        name = self.name_entry.get()
        ing = self.ing_entry.get()
        ins = self.ins_entry.get()

        error = self.validate_input(name, ing, ins)
        if error:
            self.listbox.insert("end", f"ERROR: {error}\n")
            return

        # duplicate check
        recipes = self.service.load_recipes()
        for r in recipes:
            if r["name"].lower() == name.lower():
                self.listbox.insert("end", "ERROR: Recipe already exists\n")
                return

        recipe = Recipe(name, ing, ins)
        self.service.add_recipe(recipe)

        self.refresh_list()

    def update_recipe(self):
        if self.selected_index is None:
            self.listbox.insert("end", "ERROR: No recipe selected\n")
            return

        name = self.name_entry.get()
        ing = self.ing_entry.get()
        ins = self.ins_entry.get()

        error = self.validate_input(name, ing, ins)
        if error:
            self.listbox.insert("end", f"ERROR: {error}\n")
            return

        recipe = Recipe(name, ing, ins)
        self.service.update_recipe(self.selected_index, recipe)

        self.refresh_list()

    def delete_recipe(self):
        if self.selected_index is None:
            self.listbox.insert("end", "ERROR: No recipe selected\n")
            return

        self.service.delete_recipe(self.selected_index)
        self.selected_index = None

        self.refresh_list()

    def select_recipe(self, event):
        index = int(self.listbox.index(f"@{event.x},{event.y}").split(".")[0]) - 1

        recipes = self.service.load_recipes()

        if 0 <= index < len(recipes):
            self.selected_index = index
            r = recipes[index]

            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, r["name"])

            self.ing_entry.delete(0, "end")
            self.ing_entry.insert(0, r["ingredients"])

            self.ins_entry.delete(0, "end")
            self.ins_entry.insert(0, r["instructions"])

    def refresh_list(self):
        self.listbox.delete("1.0", "end")
        recipes = self.service.load_recipes()

        for i, r in enumerate(recipes):
            self.listbox.insert("end", f"{i}. {r['name']}\n")

    def generate_report(self):
        recipes = self.service.load_recipes()
        ReportGenerator.generate_report(recipes)
        self.listbox.insert("end", "Report generated successfully\n")