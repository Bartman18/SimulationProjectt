import json
import os

class JsonReader:
    @staticmethod
    def FcfsReader():
        # Pobierz pełną ścieżkę bieżącego pliku
        current_file_path = os.path.abspath(__file__)
        # Skonstruuj ścieżkę do pliku JSON FCFS
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../fcfs_results.json")

        # Odczytaj i wydrukuj zawartość pliku JSON FCFS
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)

    @staticmethod
    def LcfsReader():
        # Pobierz pełną ścieżkę bieżącego pliku
        current_file_path = os.path.abspath(__file__)
        # Skonstruuj ścieżkę do pliku JSON LCFS
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../lcfs_results.json")

        # Odczytaj i wydrukuj zawartość pliku JSON LCFS
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)

    @staticmethod
    def FifoReader():
        # Pobierz pełną ścieżkę bieżącego pliku
        current_file_path = os.path.abspath(__file__)
        # Skonstruuj ścieżkę do pliku JSON FIFO
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../fifo_page_fault_results.json")

        # Odczytaj i wydrukuj zawartość pliku JSON FIFO
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)

    @staticmethod
    def LruReader():
        # Pobierz pełną ścieżkę bieżącego pliku
        current_file_path = os.path.abspath(__file__)
        # Skonstruuj ścieżkę do pliku JSON LRU
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../lru_page_fault_results.json")

        # Odczytaj i wydrukuj zawartość pliku JSON LRU
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)
