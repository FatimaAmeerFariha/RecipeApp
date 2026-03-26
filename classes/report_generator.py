import os

class ReportGenerator:
    @staticmethod
    def generate_report(recipes):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))

        report_dir = os.path.join(BASE_DIR, "reports")
        os.makedirs(report_dir, exist_ok=True)

        file_path = os.path.join(report_dir, "sample_report.txt")

        with open(file_path, "w") as f:
            f.write("=== RECIPE REPORT ===\n\n")

            for i, r in enumerate(recipes, 1):
                f.write(f"{i}. Name: {r['name']}\n")
                f.write(f"   Ingredients: {r['ingredients']}\n")
                f.write(f"   Instructions: {r['instructions']}\n\n")

        return file_path