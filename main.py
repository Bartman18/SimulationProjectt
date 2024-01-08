import json

from PageManager.Page import Page
from PageManager.FIFO import FIFO
from PageManager.LRU import LRU
from ProcessScheduler.ProcessGenerator import ProcessGenerator
from ProcessScheduler.Scheduler import Scheduler
from ProcessScheduler.MetricsCalculator import MetricsCalculator
from ProcessScheduler.ResultsSaver import ResultsSaver
from JsonReader.JsonReader import JsonReader
from Plot.Plots import Plots

class Main:

    @staticmethod
    def run():
        """
        Główna funkcja programu, umożliwiająca wybór opcji przez użytkownika.

        Opcje:
        1. FIFO and LRU - Page Replacement
        2. FCFS and LCFS - Process Scheduling
        3. Drawing Plots
        4. Json Reader
        5. Exit
        """
        while True:
            print("\nChoose an option:")
            print("1. FIFO and LRU - Page Replacement")
            print("2. FCFS and LCFS - Process Scheduling")
            print("3. Drawing Plots")
            print("4. Json Reader")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                Main.FifoAndLru()
            elif choice == "2":
                Main.FcfsAndLcfs()
            elif choice == "3":
                print("1. Page Replacement 2. Process Scheduling")
                nr = input("Enter the number which plot would you like to see: ")
                if nr == "1":
                    with open("lru_page_fault_results.json") as json_file:
                        lru_data = json.load(json_file)

                    with open("fifo_page_fault_results.json") as json_file:
                        fifo_data = json.load(json_file)

                    Plots.plot_comparison_fifo_lru(lru_data, fifo_data,
                                                   "Comparison of Page Faults and Hits for LRU and FIFO")

                elif nr == "2":
                    with open("fcfs_results.json") as json_file:
                        fcfs_data = json.load(json_file)

                    with open("lcfs_results.json") as json_file:
                        lcfs_data = json.load(json_file)

                    Plots.plot_comparison_fcfs_lcfs(fcfs_data["metrics"], lcfs_data["metrics"],
                                                    "Comparison of Average Waiting Time and Total Execution Time for FCFS and LCFS")

                else:
                    print("Invalid choice. Please enter a valid option")
            elif choice == "4":
                print("1. FCFS 2. LCFS 3. FIFO 4. LRU")
                nr = input("Enter the number which json would you like to read: ")
                if nr == "1":
                    JsonReader.FcfsReader()
                elif nr == "2":
                    JsonReader.LcfsReader()
                elif nr == "3":
                    JsonReader.FifoReader()
                elif nr == "4":
                    JsonReader.LruReader()
                else:
                    print("Invalid choice. Please enter a valid option")

            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def FcfsAndLcfs():
        """
        Simulates FCFS (First Come First Serve) and LCFS (Last Come First Serve) for generated processes.

        The user is asked for the number of processes, and then both CPU scheduling algorithms are simulated.
        Metrics are calculated, displayed, and saved to JSON files.
        """
        num_processes = int(input("Enter the number of processes: "))
        processes = ProcessGenerator.generate_processes(num_processes)

        Scheduler.simulate_fcfs(processes)
        fcfs_metrics = MetricsCalculator.calculate_metrics(processes)
        print("\nFCFS Metrics:")
        print(f"Average Waiting Time: {fcfs_metrics[0]}")
        print(f"Average Finish Time: {fcfs_metrics[1]}")
        print(f"Total Execution Time: {fcfs_metrics[2]}")
        print(f"Total Waiting Time: {fcfs_metrics[3]}")
        print(f"Total Turnaround Time: {fcfs_metrics[4]}")
        ResultsSaver.save_results_to_json("fcfs_results.json", processes)

        processes = ProcessGenerator.generate_processes(num_processes)
        Scheduler.simulate_lcfs(processes)
        lcfs_metrics = MetricsCalculator.calculate_metrics(processes)
        print("\nLCFS Metrics:")
        print(f"Average Waiting Time: {lcfs_metrics[0]}")
        print(f"Average Finish Time: {lcfs_metrics[1]}")
        print(f"Total Execution Time: {lcfs_metrics[2]}")
        print(f"Total Waiting Time: {lcfs_metrics[3]}")
        print(f"Total Turnaround Time: {lcfs_metrics[4]}")
        ResultsSaver.save_results_to_json("lcfs_results.json", processes)

    @staticmethod
    def FifoAnd
