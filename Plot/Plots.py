import json
import os
import matplotlib.pyplot as plt

class Plots:
    @staticmethod
    def plot_comparison_fifo_lru(json_data1, json_data2, title):
        # Definicja kategorii i wartości dla pierwszego zestawu danych (LRU)
        categories = ["Page Faults", "Hits"]
        values1 = [json_data1["page_faults"], json_data1["hits"]]

        # Definicja kategorii i wartości dla drugiego zestawu danych (FIFO)
        values2 = [json_data2["page_faults"], json_data2["hits"]]

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
                            xytext=(0, 3),  # 3 punkty przesunięcia pionowe
                            textcoords="offset points",
                            ha='center', va='bottom')

        plt.show()

    @staticmethod
    def plot_comparison_fcfs_lcfs(json_data1, json_data2, title):
        # Definicja kategorii i wartości dla pierwszego zestawu danych (FCFS)
        categories = ["Average Waiting Time", "Total Execution Time"]
        values1 = [json_data1["average_waiting_time"], json_data1["total_turnaround_time"]]

        # Definicja kategorii i wartości dla drugiego zestawu danych (LCFS)
        values2 = [json_data2["average_waiting_time"], json_data2["total_turnaround_time"]]

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
                            xytext=(0, 3),  # 3 punkty przesunięcia pionowe
                            textcoords="offset points",
                            ha='center', va='bottom')

        plt.show()


