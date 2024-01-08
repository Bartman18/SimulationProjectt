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

        for i in range(len(incoming_stream)):
            if incoming_stream[i] in self.s:
                self.hits += 1
            elif len(self.s) < self.frames:
                self.s.add(incoming_stream[i])
                self.page_faults += 1
                self.queue.put(incoming_stream[i])
            else:
                val = self.queue.queue[0]
                self.queue.get()
                self.s.remove(val)
                self.s.add(incoming_stream[i])
                self.queue.put(incoming_stream[i])
                self.page_faults += 1

            print(incoming_stream[i], end="\t\t")
            for q_item in self.queue.queue:
                print(q_item, end="\t")
            print()

        self.save_results_to_json("fifo")
