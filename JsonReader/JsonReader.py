import json

import json
import os


class JsonReader:
    @staticmethod
    def FcfsReader():
        current_file_path = os.path.abspath(__file__)
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../fcfs_results.json")

        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)

    @staticmethod
    def LcfsReader():
        current_file_path = os.path.abspath(__file__)
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../lcfs_results.json")

        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)

    @staticmethod
    def FifoReader():
        current_file_path = os.path.abspath(__file__)
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../fifo_page_fault_results.json")

        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)

    @staticmethod
    def LruReader():
        current_file_path = os.path.abspath(__file__)
        json_file_path = os.path.join(os.path.dirname(current_file_path), "../lru_page_fault_results.json")

        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            formatted_json = json.dumps(json_data, indent=2)
            print(formatted_json)
