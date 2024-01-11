from PageManager.Page import Page
from queue import Queue

class FIFO(Page):
    def __init__(self, frames):
        """
        Inicjalizuje obiekt klasy FIFO, dziedziczący po klasie Page, reprezentujący algorytm zastępowania stron FIFO.

        :param frames: Liczba ramek dostępnych w systemie.
        """
        super().__init__(frames)
        self.queue = Queue()

    def run(self, incoming_stream):
        """
        Uruchamia symulację algorytmu zastępowania stron FIFO na podstawie danego strumienia stron.

        :param incoming_stream: Strumień przychodzących stron.
        """
        print("Incoming \t pages")

        # Iteracja przez strumień przychodzących stron
        for i in range(len(incoming_stream)):
            # Sprawdzenie, czy strona już znajduje się w pamięci (hit)
            if incoming_stream[i] in self.s:
                self.hits += 1
            # Jeśli strona nie znajduje się w pamięci
            elif len(self.s) < self.frames:  # Sprawdzenie, czy istnieje wolne miejsce w pamięci
                self.s.add(incoming_stream[i])  # Dodanie strony do pamięci
                self.page_faults += 1  # Zwiększenie liczby błędów strony
                self.queue.put(incoming_stream[i])  # Dodanie strony do kolejki
            else:
                # Jeśli brak miejsca w pamięci, należy zastąpić najstarszą stronę (FIFO)
                val = self.queue.queue[0]  # Pobranie najstarszej strony z kolejki(pierwsza, która została dodana)
                self.queue.get()  # Usunięcie najstarszej strony z kolejki
                self.s.remove(val)  # Usunięcie najstarszej strony z pamięci
                self.s.add(incoming_stream[i])  # Dodanie nowej strony do pamięci
                self.queue.put(incoming_stream[i])  # Dodanie nowej strony do kolejki
                self.page_faults += 1  # Zwiększenie liczby błędów strony

            # Wyświetlanie informacji na temat przychodzących stron i stanu pamięci
            print(incoming_stream[i], end="\t\t")
            for q_item in self.queue.queue:
                print(q_item, end="\t")
            print()

        # Zapisanie wyników do pliku JSON
        self.save_results_to_json("fifo")
