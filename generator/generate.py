import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["animal", "age", "weight_kg", "enclosure", "diet_type"]


def generate_row():
    animals = ["Панда", "Обезьяна", "Слон", "Жираф", "Лев", "Тигр", "Зебра", "Кенгуру", "Пингвин", "Фламинго"]
    diets = ["травоядное", "хищное", "всеядное"]
    enclosures = ["Африка", "Азия", "Австралия", "Хищники", "Экзотические птицы"]

    return {
        "animal": random.choice(animals),
        "age": random.randint(1, 20),
        "weight_kg": round(random.uniform(2.5, 500.0), 1),
        "enclosure": random.choice(enclosures),
        "diet_type": random.choice(diets),
    }


OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)