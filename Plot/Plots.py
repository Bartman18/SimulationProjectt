import json
import os
import matplotlib.pyplot as plt

class Plots:

    @staticmethod
    def plot_comparison_fifo_lru(json_data1, json_data2, title):
        categories = ["Page Faults", "Hits"]
        values1 = [json_data1["page_faults"], json_data1["hits"]]
        values2 = [json_data2["page_faults"], json_data2["hits"]]  # <-- Closing square bracket here

        # Stwórz dwie kolumny na wykresie
        width = 0.35
        fig, ax = plt.subplots()
        bar1 = ax.bar([i - width/2 for i in range(len(categories))], values1, width, label='LRU')
        bar2 = ax.bar([i + width/2 for i in range(len(categories))], values2, width, label='FIFO')

        # Dodaj etykiety, tytuły itp.
        ax.set_title(title)
        ax.set_xlabel("Kategorie")
        ax.set_ylabel("Wartości")
        ax.set_xticks(range(len(categories)))
        ax.set_xticklabels(categories)
        ax.legend()

        # Dodaj etykiety na słupkach
        for bar in [bar1, bar2]:
            for rect in bar:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        plt.show()

    @staticmethod
    def plot_comparison_fcfs_lcfs(json_data1, json_data2, title):
        categories = ["Average Waiting Time", "Total Execution Time"]
        values1 = [json_data1["average_waiting_time"], json_data1["total_execution_time"]]
        values2 = [json_data2["average_waiting_time"], json_data2["total_execution_time"]]

        # Stwórz dwie kolumny na wykresie
        width = 0.35
        fig, ax = plt.subplots()
        bar1 = ax.bar([i - width/2 for i in range(len(categories))], values1, width, label='FCFS')
        bar2 = ax.bar([i + width/2 for i in range(len(categories))], values2, width, label='LCFS')

        # Dodaj etykiety, tytuły itp.
        ax.set_title(title)
        ax.set_xlabel("Kategorie")
        ax.set_ylabel("Wartości")
        ax.set_xticks(range(len(categories)))
        ax.set_xticklabels(categories)
        ax.legend()

        # Dodaj etykiety na słupkach
        for bar in [bar1, bar2]:
            for rect in bar:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        plt.show()

if __name__ == "__main__":
    # Wczytaj dane z plików JSON z odpowiednich lokalizacji
    current_file_path = os.path.abspath(__file__)
    lru_json_path = os.path.join(os.path.dirname(current_file_path), "../lru_page_fault_results.json")
    fifo_json_path = os.path.join(os.path.dirname(current_file_path), "../fifo_page_fault_results.json")
    lcfs_json_path = os.path.join(os.path.dirname(current_file_path), "../lcfs_results.json")
    fcfs_json_path = os.path.join(os.path.dirname(current_file_path), "../fcfs_results.json")

    with open(lru_json_path) as json_file:
        lru_data = json.load(json_file)

    with open(fifo_json_path) as json_file:
        fifo_data = json.load(json_file)

    with open(lcfs_json_path) as json_file:
        lcfs_data = json.load(json_file)

    with open(fcfs_json_path) as json_file:
        fcfs_data = json.load(json_file)

    # Rysuj wykresy słupkowe z wczytanych danych
    Plots.plot_comparison_fifo_lru(lru_data, fifo_data, "Porównanie Page Faults i Hits dla LRU i FIFO")
    Plots.plot_comparison_fcfs_lcfs(fcfs_data["metrics"], lcfs_data["metrics"], "Porównanie Average Waiting Time i Total Execution Time dla FCFS i LCFS")
