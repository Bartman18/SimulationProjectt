import numpy as np
from ProcessScheduler.Process import Process

class ProcessGenerator:
    @staticmethod
    def generate_processes(num_processes):
        """
        Generuje losowe procesy do symulacji.

        :param num_processes: Liczba procesów do wygenerowania.
        :return: Lista obiektów klasy Process reprezentujących procesy.
        """
        # Generowanie losowych czasów przyjścia i wykonania dla procesów
        arrival_times = np.random.randint(0, 11, num_processes)
        execution_times = np.random.randint(1, 11, num_processes)

        # Tworzenie obiektów klasy Process na podstawie wygenerowanych danych
        processes = [Process(i + 1, arrival_times[i], execution_times[i]) for i in range(num_processes)]
        return processes
