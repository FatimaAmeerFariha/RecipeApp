# main.py
from classes.recipe_service import RecipeService

def main():
    service = RecipeService()

    while True:
        print("\n--- Recipe App ---")
        print("1. Add Recipe")
        print("2. List Recipes")
        print("3. View Recipe")
        print("4. Delete Recipe")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter recipe title: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            ingredients = [i.strip() for i in ingredients]
            instructions = input("Enter instructions: ")
            service.add_recipe(title, ingredients, instructions)

        elif choice == "2":
            service.list_recipes()

        elif choice == "3":
            service.list_recipes()
            idx = int(input("Enter recipe number to view: ")) - 1
            service.view_recipe(idx)

        elif choice == "4":
            service.list_recipes()
            idx = int(input("Enter recipe number to delete: ")) - 1
            service.delete_recipe(idx)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()