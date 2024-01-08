import json
import numpy as np

class Page:
    def __init__(self, frames):
        """
        Inicjalizuje obiekt klasy Page, reprezentujący system stron.

        :param frames: Liczba ramek dostępnych w systemie.
        """
        self.frames = frames
        self.s = set()              # Zbiór przechowujący aktualnie załadowane strony.
        self.page_faults = 0        # Liczba błędów strony (page faults).
        self.hits = 0               # Liczba trafień (hits).

    def reset(self):
        """
        Resetuje stan obiektu klasy Page.

        Usuwa wszystkie załadowane strony oraz zeruje liczniki błędów strony i trafień.
        """
        self.s.clear()
        self.page_faults = 0
        self.hits = 0

    def generate_random_stream(self, num_pages):
        """
        Generuje losowy strumień numerów stron.

        :param num_pages: Liczba stron do wygenerowania w strumieniu.
        :return: Lista z numerami stron.
        """
        return list(np.random.randint(0, 10, size=num_pages))

    def save_results_to_json(self, algorithm_name):
        """
        Zapisuje wyniki błędów strony do pliku JSON.

        :param algorithm_name: Nazwa algorytmu użytego do zarządzania stronami.
        """
        results = {
            "algorithm": algorithm_name,
            "frame_size": self.frames,
            "page_faults": self.page_faults,
            "hits": self.hits
        }

        with open(f"{algorithm_name}_page_fault_results.json", "w") as json_file:
            json.dump(results, json_file, indent=2)
