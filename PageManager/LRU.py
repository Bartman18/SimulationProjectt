from collections import deque
from PageManager.Page import Page

class LRU(Page):
    def __init__(self, frames):
        """
        Inicjalizuje obiekt klasy LRU, dziedziczący po klasie Page, reprezentujący algorytm zastępowania stron LRU.

        :param frames: Liczba ramek dostępnych w systemie.
        """
        super().__init__(frames)
        self.queue = deque()

    def run(self, incoming_stream):
        """
        Uruchamia symulację algorytmu zastępowania stron LRU na podstawie danego strumienia stron.

        :param incoming_stream: Strumień przychodzących stron.
        """
        print("Incoming \t pages")

        # Iteracja przez strumień przychodzących stron
        for i in range(len(incoming_stream)):
            if incoming_stream[i] in self.s:
                # Strona jest już w pamięci (hit)
                self.hits += 1
                self.queue.remove(incoming_stream[i])  # Usunięcie strony z kolejki LRU
            elif len(self.s) < self.frames:
                # Błąd strony, ale jest miejsce w pamięci
                self.page_faults += 1
            else:
                # Błąd strony, trzeba zastąpić stronę w pamięci (LRU)
                val = self.queue.popleft()  # Usunięcie najstarszej strony z kolejki LRU(najdawniej używaną stronę)
                self.s.remove(val)  # Usunięcie najstarszej strony z pamięci
                self.page_faults += 1

            self.s.add(incoming_stream[i])  # Dodanie nowej strony do pamięci
            self.queue.append(incoming_stream[i])  # Dodanie nowej strony do kolejki LRU

            # Wyświetlanie informacji na temat przychodzących stron i stanu pamięci
            print(incoming_stream[i], end="\t\t")
            for q_item in self.queue:
                print(q_item, end="\t")
            print()

            if len(self.queue) > self.frames:
                self.queue.popleft()  # Usunięcie najstarszej strony z kolejki LRU, jeśli przekroczyła rozmiar ramek

        # Zapisanie wyników do pliku JSON
        self.save_results_to_json("lru")