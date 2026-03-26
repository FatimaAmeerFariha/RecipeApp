# 📄 README.md – Recipe Management Application

## 📌 Project Title

**Recipe Management Application (Python + Custom GUI)**

---

## 📖 Project Description

This is a **Recipe Management Application** built using **Python OOP principles** with a modern GUI using **CustomTkinter**.

The application allows users to:

* Add new recipes with name, ingredients, and instructions
* Store recipes persistently using a JSON file
* View and manage saved recipes
* Generate a structured recipe report (text file)

The project focuses on **clean architecture, proper file handling, and OOP design**, making it scalable, maintainable, and suitable for academic purposes.

---

## 🧠 OOP Concepts Used

* **Encapsulation** – Recipe data is stored inside `Recipe` objects
* **Inheritance** – GUI structure extends a base class (`BaseWindow`)
* **Composition** – `RecipeApp` uses `RecipeService` and `ReportGenerator`
* **Abstraction** – Data handling and UI logic are separated

---

## 🏗️ Class Structure Overview

| Class Name      | Purpose                                        |
| --------------- | ---------------------------------------------- |
| BaseWindow      | Parent GUI class for common window setup       |
| RecipeApp       | Main GUI controller handling user interactions |
| RecipeService   | Handles saving/loading recipes using JSON      |
| Recipe          | Represents a single recipe object              |
| ReportGenerator | Generates a text report of all saved recipes   |

---

## 🗂️ Project File Structure

```
RecipeApp/
│── main.py
│── README.md
│
├── data/
│   └── recipes.json        # Stores all recipes
│
├── classes/
│   ├── __init__.py
│   ├── base_window.py
│   ├── recipe_app.py
│   ├── recipe_service.py
│   ├── recipe.py
│   ├── report_generator.py
│
├── reports/
│   └── sample_report.txt   # Generated report output
```

---

## 💻 Technologies Used

* Python 3
* CustomTkinter (GUI framework)
* JSON (for data storage)
* File handling (for reports)

---

## ▶️ How to Run

1. Install dependencies:

```
pip install customtkinter
```

2. Run the application:

```
python main.py
```

---

## 📊 Features

✔ Add new recipes
✔ Store recipes in JSON file (`data/recipes.json`)
✔ Persistent data (data saved even after closing app)
✔ Generate recipe report (`reports/sample_report.txt`)
✔ Clean OOP-based architecture
✔ Simple and user-friendly GUI

---

## 📄 Sample Recipe Report

```
=== RECIPE REPORT ===

1. Name: Chocolate Cake
   Ingredients: Flour, Cocoa, Sugar, Eggs
   Instructions: Mix and bake

2. Name: Vegetable Stir Fry
   Ingredients: Broccoli, Carrot, Soy Sauce
   Instructions: Stir fry all ingredients
```

---

## ⚙️ Notes

* The `data/recipes.json` file is automatically created if not found
* The `reports/` folder is generated automatically when creating reports
* All file paths are dynamically handled to avoid errors in different environments (like VS Code)

---

## 🚀 Future Improvements

* Add recipe search functionality
* Add delete/update options
* Display recipe list in GUI
* Add categories and filtering
* Improve UI styling

---
