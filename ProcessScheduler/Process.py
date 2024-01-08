class Process:
    def __init__(self, process_id, arrival_time, execution_time):
        """
        Inicjalizacja obiektu klasy Process.

        :param process_id: Unikalny identyfikator procesu.
        :param arrival_time: Czas przyjścia procesu do systemu.
        :param execution_time: Czas wymagany do wykonania procesu.
        """
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.waiting_time = 0  # Czas oczekiwania na wykonanie procesu.
        self.finish_time = 0   # Czas zakończenia wykonania procesu.
