import json
import os


class FileHandler:

    @staticmethod
    def load_data(filename):
        try:
            if not os.path.exists(filename):
                return []

            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

                return []

        except (json.JSONDecodeError, OSError):
            return []

    @staticmethod
    def save_data(filename, data):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except OSError as e:
            print(f"Error saving data: {e}")