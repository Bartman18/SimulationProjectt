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

        for i in range(len(incoming_stream)):
            if incoming_stream[i] in self.s:
                # Strona jest już w ramce
                self.hits += 1
                self.queue.remove(incoming_stream[i])
            elif len(self.s) < self.frames:
                # Błąd strony, ale jest miejsce w ramkach
                self.page_faults += 1
            else:
                # Błąd strony, trzeba zastąpić stronę w ramkach
                val = self.queue.popleft()
                self.s.remove(val)
                self.page_faults += 1

            self.s.add(incoming_stream[i])
            self.queue.append(incoming_stream[i])

            print(incoming_stream[i], end="\t\t")
            for q_item in self.queue:
                print(q_item, end="\t")
            print()

            if len(self.queue) > self.frames:
                self.queue.popleft()

        self.save_results_to_json("lru")
