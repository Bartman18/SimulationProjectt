import json
import numpy as np


class ResultsSaver:
    @staticmethod
    def save_results_to_json(filename, processes):
        """
        Zapisuje wyniki symulacji do pliku JSON.

        :param filename: Nazwa pliku, do którego mają zostać zapisane wyniki.
        :param processes: Lista obiektów klasy Process reprezentujących procesy w symulacji.
        """
        def convert_np_types(obj):
            """
            Konwertuje obiekty NumPy na standardowe typy Pythona.

            :param obj: Obiekt do konwersji.
            :return: Skonwertowany obiekt.
            """
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return obj

        results = {
            "processes": []
        }

        # Zapisywanie informacji o poszczególnych procesach
        for process in processes:
            process_info = {
                "process_id": process.process_id,
                "arrival_time": process.arrival_time,
                "waiting_time": process.waiting_time,
                "finish_time": process.finish_time
            }
            results["processes"].append(process_info)

        # Obliczenia dodatkowych metryk
        waiting_times = np.array([process.waiting_time for process in processes])
        finish_times = np.array([process.finish_time for process in processes])

        average_waiting_time = np.mean(waiting_times)
        average_finish_time = np.mean(finish_times)
        total_execution_time = np.sum([process.execution_time for process in processes])
        total_turnaround_time = np.sum(finish_times - np.array([process.arrival_time for process in processes]))

        results["metrics"] = {
            "average_waiting_time": average_waiting_time,
            "average_finish_time": average_finish_time,
            "total_execution_time": total_execution_time,
            "total_waiting_time": np.sum(waiting_times),
            "total_turnaround_time": total_turnaround_time
        }

        # Zapisywanie wyników do pliku JSON
        with open(filename, 'w') as json_file:
            json.dump(results, json_file, default=convert_np_types, indent=2)
