import sys
from algorithms.fcfs import simulate_fcfs
from algorithms.c_scan import simulate_c_scan
from algorithms.c_look import simulate_c_look
from statistics import aggregate_statistics, display_summary
from utils.input_handling import get_initial_position, get_track_requests
from utils.display import display_results

def main():
    """
    Entry point for the Disk Scheduling Simulator application.
    """
    print("Welcome to the Disk Scheduling Simulator.")

    initial_position = get_initial_position()
    file_path = input("Enter the file path for track request sequence: ")
    track_requests = get_track_requests(file_path)

    disk_size = 200  # Default disk size; can be modified if required.

    # Collect results for all algorithms
    results = {}

    # Execute FCFS algorithm
    total_fcfs, service_fcfs = simulate_fcfs(initial_position, track_requests, disk_size)
    results["First-Come, First-Served (FCFS)"] = (total_fcfs, service_fcfs)
    display_results("First-Come, First-Served (FCFS)", total_fcfs, service_fcfs)

    # Execute C-SCAN algorithm
    total_c_scan, service_c_scan = simulate_c_scan(initial_position, track_requests, disk_size)
    results["Circular SCAN (C-SCAN)"] = (total_c_scan, service_c_scan)
    display_results("Circular SCAN (C-SCAN)", total_c_scan, service_c_scan)

    # Execute C-LOOK algorithm
    total_c_look, service_c_look = simulate_c_look(initial_position, track_requests, disk_size)
    results["Circular LOOK (C-LOOK)"] = (total_c_look, service_c_look)
    display_results("Circular LOOK (C-LOOK)", total_c_look, service_c_look)

    # Generate and display statistics
    statistics = aggregate_statistics(results)
    display_summary(statistics)

if __name__ == "__main__":
    main()
