class Scheduler:
    @staticmethod
    def simulate_fcfs(processes):
        """
        Symulacja algorytmu planowania First Come First Serve (FCFS).

        :param processes: Lista obiektów reprezentujących procesy.
        """
        # Inicjalizacja bieżącego czasu
        current_time = 0

        # Sortowanie procesów względem czasu przyjścia (rosnąco)
        processes.sort(key=lambda x: x.arrival_time)

        # Iteracja przez posortowane procesy
        for process in processes:
            # Aktualizacja bieżącego czasu, jeśli proces przybywa później
            if process.arrival_time > current_time:
                current_time = process.arrival_time

            # Obliczenie czasu oczekiwania i zakończenia dla procesu
            process.waiting_time = current_time - process.arrival_time
            process.finish_time = current_time + process.execution_time

            # Aktualizacja bieżącego czasu na czas zakończenia procesu
            current_time = process.finish_time

    @staticmethod
    def simulate_lcfs(processes):
        """
        Symulacja algorytmu planowania Last Come First Serve (LCFS).

        :param processes: Lista obiektów reprezentujących procesy.
        """
        # Inicjalizacja bieżącego czasu
        current_time = 0

        # Sortowanie procesów względem czasu przyjścia (rosnąco) i odwrócenie kolejności
        processes.sort(key=lambda x: x.arrival_time)
        processes.reverse()

        # Iteracja przez posortowane i odwrócone procesy
        for process in processes:
            # Aktualizacja bieżącego czasu, jeśli proces przybywa później
            if process.arrival_time > current_time:
                current_time = process.arrival_time

            # Obliczenie czasu oczekiwania i zakończenia dla procesu
            process.waiting_time = current_time - process.arrival_time
            process.finish_time = current_time + process.execution_time

            # Aktualizacja bieżącego czasu na czas zakończenia procesu
            current_time = process.finish_time
