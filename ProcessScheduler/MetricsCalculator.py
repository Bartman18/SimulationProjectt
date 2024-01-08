import numpy as np
import numpy as np

class MetricsCalculator:
    @staticmethod
    def calculate_metrics(processes):
        """
        Oblicza różne metryki związane z wykonaniem procesów.

        :param processes: Lista obiektów klasy Process reprezentujących procesy.
        :return: Krotka zawierająca następujące metryki:
                 (average_waiting_time, average_finish_time, total_execution_time,
                  total_waiting_time, total_turnaround_time).
        """
        waiting_times = np.array([process.waiting_time for process in processes])
        finish_times = np.array([process.finish_time for process in processes])

        average_waiting_time = np.mean(waiting_times)
        average_finish_time = np.mean(finish_times)
        total_execution_time = np.sum([process.execution_time for process in processes])
        total_turnaround_time = np.sum(finish_times - np.array([process.arrival_time for process in processes]))

        return average_waiting_time, average_finish_time, total_execution_time, np.sum(waiting_times), total_turnaround_time

    @staticmethod
    def print_metrics(metrics):
        """
        Wyświetla na konsoli różne metryki związane z wykonaniem procesów.

        :param metrics: Słownik zawierający metryki do wyświetlenia.
        """
        print(f"Average Waiting Time: {metrics['average_waiting_time']}")
        print(f"Average Finish Time: {metrics['average_finish_time']}")
        print(f"Total Execution Time: {metrics['total_execution_time']}")
        print(f"Total Waiting Time: {metrics['total_waiting_time']}")
        print(f"Total Turnaround Time: {metrics['total_turnaround_time']}")
