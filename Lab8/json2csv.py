import json
import csv
import sys
import os
from pathlib import Path


def json_to_csv(json_filename):
    if not os.path.exists(json_filename):
        print(f"Ошибка: Файл '{json_filename}' не найден.")
        return

    with open(json_filename, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Ошибка при чтении JSON: {e}")
            return

    csv_filename = Path(json_filename).stem + ".csv"
    json_path = Path(json_filename)
    csv_path = json_path.parent / csv_filename

    try:
        if isinstance(data, list) and len(data) > 0:
            with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

        elif isinstance(data, dict) and len(data) == 1 and isinstance(next(iter(data.values())), list):
            records = next(iter(data.values()))
            if len(records) > 0:
                with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=records[0].keys())
                    writer.writeheader()
                    writer.writerows(records)

        elif isinstance(data, dict):
            with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in data.items():
                    writer.writerow([key, value])
        else:
            print("Ошибка: Неподдерживаемый формат JSON")
            return

        print(f"Файл успешно преобразован: {csv_path}")
    except Exception as e:
        print(f"Ошибка при записи CSV: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    json_filename = sys.argv[1]
    json_to_csv(json_filename)