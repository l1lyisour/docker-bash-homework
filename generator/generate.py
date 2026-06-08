import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["name", "age", "weight", "color"]

def generate_row():
    return {
        "name": random.choice(["Пуговка", "Мурзик", "Барсик", "Луна", "Персик", "Снежок", "Рыжик", "Белка"]),
        "age": random.randint(0, 15),                  
        "weight": round(random.uniform(2.0, 7.5), 2),   
        "color": random.choice(["рыжий", "серый", "белый", "чёрный", "полосатый"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")
os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
    