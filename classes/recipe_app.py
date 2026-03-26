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

        # ---------------- MAIN FRAME ----------------
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # ---------------- LEFT FRAME (INPUTS) ----------------
        self.left_frame = ctk.CTkFrame(self.main_frame)
        self.left_frame.grid(row=0, column=0, sticky="n", padx=10)

        # ---------------- RIGHT FRAME (LIST) ----------------
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.grid(row=0, column=1, sticky="n", padx=10)

        # ---------------- TITLE ----------------
        ctk.CTkLabel(self.left_frame, text="Recipe App", font=("Arial", 20)).pack(pady=10)

        # ---------------- INPUTS ----------------
        self.name_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Recipe Name", width=400, height=40)
        self.name_entry.pack(pady=5)

        self.ing_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Ingredients", width=400, height=40)
        self.ing_entry.pack(pady=5)

        self.ins_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Instructions", width=400, height=40)
        self.ins_entry.pack(pady=5)

        self.search_entry = ctk.CTkEntry(self.left_frame, placeholder_text="Search Recipe", width=400, height=40)
        self.search_entry.pack(pady=5)

        # ---------------- BUTTONS ----------------
        ctk.CTkButton(self.left_frame, text="Search", command=self.search_recipe).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Show All", command=self.refresh_list).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Add Recipe", command=self.add_recipe).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Update Recipe", command=self.update_recipe).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Delete Recipe", command=self.delete_recipe).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Generate Report", command=self.generate_report).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Sort A-Z", command=self.sort_recipes).pack(pady=5)

        # ---------------- LISTBOX (RIGHT SIDE) ----------------
        self.listbox = ctk.CTkTextbox(self.right_frame, height=500, width=300)
        self.listbox.pack(pady=10)

        self.listbox.bind("<ButtonRelease-1>", self.select_recipe)

        self.refresh_list()

    # ---------------- ADD ----------------
    def add_recipe(self):
        name = self.name_entry.get()
        ing = self.ing_entry.get()
        ins = self.ins_entry.get()

        recipes = self.service.load_recipes()
        for r in recipes:
            if r["name"].lower() == name.lower():
                self.show_message("Recipe already exists")
                return

        self.service.add_recipe(Recipe(name, ing, ins))
        self.clear_fields()
        self.refresh_list()
        self.show_message("Recipe added")

    # ---------------- UPDATE ----------------
    def update_recipe(self):
        if self.selected_index is None:
            self.show_message("Select a recipe first")
            return

        self.service.update_recipe(
            self.selected_index,
            Recipe(self.name_entry.get(), self.ing_entry.get(), self.ins_entry.get())
        )

        self.clear_fields()
        self.refresh_list()
        self.show_message("Recipe updated")

    # ---------------- DELETE ----------------
    def delete_recipe(self):
        if self.selected_index is None:
            self.show_message("Select a recipe first")
            return

        self.service.delete_recipe(self.selected_index)
        self.selected_index = None

        self.clear_fields()
        self.refresh_list()
        self.show_message("Recipe deleted")

    # ---------------- REPORT (2ND WINDOW FIXED) ----------------
    def generate_report(self):
        recipes = self.service.load_recipes()
        path = ReportGenerator.generate_report(recipes)

        win = ctk.CTkToplevel(self)
        win.title("Recipe Report")
        win.geometry("600x450")

        ctk.CTkLabel(win, text="Recipe Report", font=("Arial", 18)).pack(pady=10)

        text = ctk.CTkTextbox(win, width=550, height=350)
        text.pack()

        with open(path, "r") as f:
            text.insert("end", f.read())

    # ---------------- SEARCH ----------------
    def search_recipe(self):
        keyword = self.search_entry.get().lower()
        recipes = self.service.load_recipes()

        self.listbox.delete("1.0", "end")

        found = False
        for i, r in enumerate(recipes):
            if keyword in r["name"].lower():
                self.listbox.insert("end", f"{i}. {r['name']}\n")
                found = True

        if not found:
            self.listbox.insert("end", "No recipe found\n")

    # ---------------- SORT ----------------
    def sort_recipes(self):
        recipes = self.service.load_recipes()
        recipes.sort(key=lambda x: x["name"].lower())

        self.listbox.delete("1.0", "end")
        for i, r in enumerate(recipes):
            self.listbox.insert("end", f"{i}. {r['name']}\n")

    # ---------------- SELECT ----------------
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

    # ---------------- HELPERS ----------------
    def refresh_list(self):
        self.listbox.delete("1.0", "end")
        for i, r in enumerate(self.service.load_recipes()):
            self.listbox.insert("end", f"{i}. {r['name']}\n")

    def show_message(self, msg):
        self.listbox.insert("end", f"{msg}\n")

    def clear_fields(self):
        self.name_entry.delete(0, "end")
        self.ing_entry.delete(0, "end")
        self.ins_entry.delete(0, "end")