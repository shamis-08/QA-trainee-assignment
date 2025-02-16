import json
import os

def load_json_data(filename: str):
    """
    Загружает данные из JSON-файла, расположенного в папке 'tests/data'.
    """
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)
